from aiogram import Bot,executor,Dispatcher,types
from aiogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyKeyboardRemove


BOT_TOKEN = ''

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])

async def start_func(m:Message):
    await bot.send_message(m.chat.id,f"Assalomu alaykum {m.from_user.full_name}")
    await m.reply('Hi friend ')



if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

