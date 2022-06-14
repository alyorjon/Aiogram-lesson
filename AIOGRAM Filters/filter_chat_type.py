from aiogram import Bot,executor,Dispatcher,types
from aiogram.types import Message,ChatType
from aiogram.dispatcher.filters import ChatTypeFilter
from config import BOT_TOKEN
BOT_TOKEN = BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# start command
@dp.message_handler(commands=['start'])
async def start_func(m:Message):
    await bot.send_message(m.chat.id,f"Assalomu alaykum {m.from_user.full_name}")
    await m.reply('Hi friend ')
@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE))
async def python_text(m:Message):
    await bot.send_message(m.chat.id,f"Your conversetion type is {m.chat.type}")
@dp.message_handler(ChatTypeFilter([ChatType.GROUP,ChatType.SUPERGROUP,ChatType.SUPER_GROUP]))
async def python_text(m:Message):
    await bot.send_message(m.chat.id,f"Your conversetion type is {m.chat.type}")

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

