from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncpg

from data.config import ADMINS
from loader import dp,userdb,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user=await userdb.add_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username

        )
    except asyncpg.exceptions.UniqueViolationError:
        user=await userdb.select_user(telegram_id=message.from_user.id)

    await message.answer("Salom bu bot eng zo'ri ")

    #adminga xabar

    msg=f"Yangi foydalanuvchi qo'shildi\n"
    msg+=f"ID :{user['telegram_id']}\n"
    msg+=f"username :@{user['username']}\n"
    await bot.send_message(ADMINS[0],msg)

