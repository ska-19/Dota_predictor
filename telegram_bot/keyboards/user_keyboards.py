from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo


def get_main_ikb() -> InlineKeyboardMarkup:
    """Get main keyboard."""
    ikb = [
        [InlineKeyboardButton(text='Получить предсказание', callback_data='get_prediction')],
    ]
    ikeyboard = InlineKeyboardMarkup(inline_keyboard=ikb)
    return ikeyboard

def get_back_button() -> InlineKeyboardMarkup:
    """Get back button."""
    ikb = [
        [InlineKeyboardButton(text="Отменить", callback_data="back")],
    ]
    ikeyboard = InlineKeyboardMarkup(inline_keyboard=ikb)
    return ikeyboard
