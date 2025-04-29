from aiogram import types
from loader import dp,bot,userdb


@dp.message_handler(commands="user")
async def bot_user(message: types.Message):
    user=await userdb.select_user(telegram_id=message.from_user.id)
    telegram_id=user['telegram_id']
    await userdb.delete_user(telegram_id=telegram_id)
