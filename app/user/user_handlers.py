import logging; import os; import time; import sys

import pyautogui
import subprocess

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.database.requests as rq
import app.user.user_keyboards as kb

client = Router()

class Input_String(StatesGroup):
    string = State()


@client.message(CommandStart())
async def start(message: Message):
    await message.answer(f"user-pc: <code>{os.getlogin()}</code>\n\n🖥 Выбери действие из меню:", 
        reply_markup=kb.main_menu,
        parse_mode="HTML")

@client.callback_query(F.data.in_(["back_main_menu"]))
async def back_main_menu(call: CallbackQuery):
    await call.message.edit_text(f"user-pc: <code>{os.getlogin()}</code>\n\n🖥 Выбери действие из меню:", 
        reply_markup=kb.main_menu,
        parse_mode="HTML")

@client.callback_query(F.data.in_(["browser", "back_browser_menu"]))
async def browser(call: CallbackQuery):
    await call.message.edit_text("Какое действие вы хотите произвести.", 
        reply_markup=kb.browser_menu)

    @client.callback_query(F.data.in_(["open_browser"]))
    async def open_browser(call: CallbackQuery):
        await call.answer("Запускаю Firefox...")

        file_path = r'C:/Program Files (x86)/Mozilla Firefox/firefox.exe'
        subprocess.Popen([file_path])

        time.sleep(2)

        pyautogui.press('enter')

        await call.answer("Firefox успешно запущен ✅")

    @client.callback_query(F.data.in_(["close_browser"]))
    async def close_browser(call: CallbackQuery):
        try:
            await call.answer("Попытка закрыть Firefox...")

            os.system('taskkill /f /im firefox.exe')

            await call.answer("FireFox успешно закрыт ✅")
        except:
            await call.answer("Не удалось закрыть FireFox 🤡")

    @client.callback_query(F.data.in_(["close_tab"]))
    async def close_tab(call: CallbackQuery):
        try:
            pyautogui.hotkey('ctrl', 'w')
            await call.answer("Вкладка успешно закрыта ✅")
        except:
            await call.answer("Не удалось закрыть вкладку 🤡")

    @client.callback_query(F.data.in_(["also_browser"]))
    async def also_browser(call: CallbackQuery):
        await call.message.edit_text("Выберите дополнительно взаимодействие с браузером",
            reply_markup=kb.also_browser)

        @client.callback_query(F.data.in_(["open_youtube"]))
        async def open_youtube(call: CallbackQuery):
            try:
                await call.answer("Попытка открыть YouTube...")

                pyautogui.hotkey('ctrl', 't')
                pyautogui.moveTo(x=736, y=68)
                pyautogui.click(button='left')
                pyautogui.write('https://youtube.com')
                pyautogui.press('enter')

                await call.answer("YouTube успешно запущен ✅")
            except:
                await call.answer("Не удалось открыть YouTube 🤡")

        @client.callback_query(F.data.in_(["open_user"]))
        async def open_user(call: CallbackQuery, state: FSMContext):
            await state.set_state(Input_String.string)
            await call.message.answer("Отправьте ссылку или введите запрос (на Англиском).")

            @client.message(Input_String.string)
            async def input_string(message: Message, state: FSMContext):
                await state.update_data(string=message.text)
                data = await state.get_data()

                pyautogui.hotkey('ctrl', 't')
                pyautogui.moveTo(x=736, y=68)
                pyautogui.click(button='left')
                pyautogui.write(f'{data["string"]}')
                pyautogui.press('enter')

                await message.answer(f"<code>{data["string"]}</code> успешно открыт ✅",
                    parse_mode="HTML")

                await state.clear()

                await message.answer("Выберите дополнительно взаимодействие с браузером", 
                    reply_markup=kb.also_browser)

@client.callback_query(F.data.in_(["tab"]))
async def tab(call: CallbackQuery):
    await call.message.edit_text("Выберите программу для открытия вкладки.",
        reply_markup=kb.open_tab_program)

    @client.callback_query(F.data.in_(["firefox_tab"]))
    async def firefox_tab(call: CallbackQuery):
        pyautogui.hotkey('win', '8')

    @client.callback_query(F.data.in_(["discord_tab"]))
    async def discord_tab(call: CallbackQuery):
        pyautogui.hotkey('win', '4')

    @client.callback_query(F.data.in_(["telegram_tab"]))
    async def telegram_tab(call: CallbackQuery):
        pyautogui.hotkey('win', '3')