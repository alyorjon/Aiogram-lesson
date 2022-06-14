from aiogram import Bot,executor,Dispatcher,types
from aiogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyKeyboardRemove

from config import BOT_TOKEN
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

def inline_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(InlineKeyboardButton(text='Button 1',callback_data='button1'),InlineKeyboardButton("Share",url='https://t.me/Alyor_python_developer'),InlineKeyboardButton("Share 2",switch_inline_query='/start'))
    return btn
@dp.message_handler(commands=['start'])
async def start_func(m:Message):
    await bot.send_message(m.chat.id,f"Assalomu alaykum {m.from_user.full_name}",reply_markup=inline_btn())
    
@dp.callback_query_handler()
async def start_1(call:types.CallbackQuery):
    await bot.send_message(call.message.chat.id,f"Message {call.data}")

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

