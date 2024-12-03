import logging

from app.database.models import async_session
from app.database.models import Lesson, CallSchlude, User
from sqlalchemy import select, update


async def set_user(user_id, user_name):
    user_name = f"@{user_name.lower()}"
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == user_id))

        if not user:
            session.add(User(id = user_id, user_name = user_name))
            await session.commit()


async def get_schlude(type_week, type_day):
    async with async_session() as session:
        result = await session.execute(select(Lesson).filter(Lesson.week == type_week, Lesson.day == type_day, Lesson.name != '-'))
        data = result.scalars().all()

        if data:
            schlude_str = f"Вот расписание.\n\n"
            for lesson in data:
                schlude_str += (f"Номер: {lesson.count}\n"
                                f"Время: {lesson.time}\n"
                                f"Предмет: {lesson.name}\n"
                                f"Кабинет: {lesson.classroom}\n"
                                f"Преподаватель: {lesson.teacher}\n\n")
                
            return schlude_str
        else:
            return "Нет занятий!"


async def get_time_lesson():
    async with async_session() as session:
        data = await session.scalar(select(CallSchlude))
        result = f"""Расписание звонков:\n\n
1 пара: {data.first_lesson}\n\n2 пара: {data.second_lesson}\n\n3 пара: {data.third_lesson}\n\n
4 пара: {data.fourth_lesson}\n\n5 пара: {data.fifth_lesson}\n\n6 пара: {data.sixth_lesson}"""

        return result


async def get_profile(user_id):
    async with async_session() as session:
        logging.info(f"Fetching profile for user_id: {user_id}")
        data = await session.scalar(select(User).where(User.id == user_id))
        result = f"👤 {data.user_name}\n\nПобеды: {data.wins}\nПроигрыши: {data.loses}\n\nprofile ID: {data.id}"

        return result
    

async def add_point(user_id):
    async with async_session() as session:
        stmt = update(User).where(User.id == user_id).values(wins=User.wins + 1)
        await session.execute(stmt)
        await session.commit()


async def del_point(user_id):
    async with async_session() as session:
        stmt = update(User).where(User.id == user_id).values(loses=User.loses + 1)
        await session.execute(stmt)
        await session.commit()


async def update_lessons(type_week, type_day, count, time, name, classroom, teacher):
    async with async_session() as session:
        stmt = update(Lesson).where(Lesson.count == count, Lesson.week == type_week, Lesson.day == type_day).values(count=count, time=time, name=name, classroom=classroom, teacher=teacher)
        await session.execute(stmt)
        await session.commit()

async def update_calls(first_lesson, second_lesson, third_lesson, fourth_lesson, fifth_lesson, sixth_lesson):
    async with async_session() as session:
        stmt = update(CallSchlude).where(CallSchlude.id == 1).values(first_lesson=first_lesson, second_lesson=second_lesson, third_lesson=third_lesson, fourth_lesson=fourth_lesson, fifth_lesson=fifth_lesson, sixth_lesson=sixth_lesson)
        await session.execute(stmt)
        await session.commit()