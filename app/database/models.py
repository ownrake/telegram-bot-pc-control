from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url = "sqlite+aiosqlite:///database.sqlite3")

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Week(Base):
    __tablename__ = "weeks"

    week: Mapped[str] = mapped_column(String(12), primary_key = True, server_default = "-")


class Day(Base):
    __tablename__ = "days"
    
    day: Mapped[str] = mapped_column(String(12), primary_key = True, server_default = "-")


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key = True)
    week: Mapped[str] = mapped_column(ForeignKey("weeks.week"))
    day: Mapped[str] = mapped_column(ForeignKey("days.day"))
    count: Mapped[str] = mapped_column(String(12), server_default = "-")
    time: Mapped[str] = mapped_column(String(24), server_default = "-")
    name: Mapped[str] = mapped_column(String(255), server_default = "-")
    classroom: Mapped[str] = mapped_column(String(12), server_default = "-")
    teacher: Mapped[str] = mapped_column(String(24), server_default = "-")


class CallSchlude(Base):
    __tablename__ = "countingLesson"

    id: Mapped[int] = mapped_column(primary_key = True)
    first_lesson: Mapped[str] = mapped_column(String(48), server_default = "-")
    second_lesson: Mapped[str] = mapped_column(String(48), server_default = "-")
    third_lesson: Mapped[str] = mapped_column(String(48), server_default = "-")
    fourth_lesson: Mapped[str] = mapped_column(String(48), server_default = "-")
    fifth_lesson: Mapped[str] = mapped_column(String(48), server_default = "-")
    sixth_lesson: Mapped[str] = mapped_column(String(48), server_default = "-")


class User(Base):
    __tablename__ = "users"

    id = mapped_column(BigInteger, primary_key = True)
    user_name: Mapped[str] = mapped_column(String(255))
    wins: Mapped[int] = mapped_column(server_default = "0")
    loses: Mapped[int] = mapped_column(server_default = "0")


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


