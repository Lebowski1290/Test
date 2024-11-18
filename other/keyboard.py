from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')],

],
    resize_keyboard=True,
    input_field_placeholder='')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='play', url='https://lebowski1290.github.io/mc/')]
])