from aiogram import Bot,executor,Dispatcher,types
from aiogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from config import BOT_TOKEN
BOT_TOKEN = BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# start command
@dp.message_handler(commands=['start'])
async def start_func(m:Message):
    await bot.send_message(m.chat.id,f"Assalomu alaykum {m.from_user.full_name}")
    await m.reply('Hi friend ')
@dp.message_handler(Text(equals="python"))
async def python_text(m:Message):
    await bot.send_message(m.chat.id,f"Your wrote {m.text}")
@dp.message_handler(Text(startswith="aiogram"))
async def python_text(m:Message):
    await bot.send_message(m.chat.id,f"Your wrote {m.text}")
@dp.message_handler(Text(endswith="telebot"))
async def python_text(m:Message):
    await bot.send_message(m.chat.id,f"Your wrote {m.text}")

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

