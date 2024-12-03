from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Действия с браузером", callback_data="browser")],
    [InlineKeyboardButton(text="Вкладки программ", callback_data="tab")]
])

browser_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📍 Открыть", callback_data="open_browser")],
    [InlineKeyboardButton(text="📍 Закрыть", callback_data="close_browser")],
    [InlineKeyboardButton(text="📍 Закрыть вкладку", callback_data="close_tab")],
    [InlineKeyboardButton(text="📍 Дополнительно", callback_data="also_browser")],
    [InlineKeyboardButton(text="«", callback_data="back_main_menu")]
])

also_browser = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📍 YouTube", callback_data="open_youtube")],
    [InlineKeyboardButton(text="📍 Свой вариант", callback_data="open_user")],
    [InlineKeyboardButton(text="«", callback_data="back_browser_menu")]
])

open_tab_program = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Firefox", callback_data="firefox_tab")],
    [InlineKeyboardButton(text="Discord", callback_data="discord_tab")],
    [InlineKeyboardButton(text="Telegram", callback_data="telegram_tab")],
    [InlineKeyboardButton(text="«", callback_data="back_main_menu")]
])