from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import other.keyboard as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'hi {message.from_user.first_name}',
                        reply_markup=kb.settings)