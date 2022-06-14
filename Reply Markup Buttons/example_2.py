"""
This is an example with usage of ReplyKeyboardMarkup
"""


from aiogram import Bot,Dispatcher,executor,filters,types
from config import BOT_TOKEN
from aiogram.types import Message,ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,ChatType
from aiogram.dispatcher.filters import Command,CommandStart,ChatTypeFilter

#Start bot
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)
def START_BTN():
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Button 1','Button 2','Button 3','Button 4','Button 5','Button 6']
    for i in buttons:
        button.insert(KeyboardButton(i))
    return button

# Command start function
@dp.message_handler(filters.Command('start'),filters.ChatTypeFilter(ChatType.PRIVATE))
async def start_func_in_private(message:Message):
    text = "It is easy example for get contact and location"
    await bot.send_message(message.chat.id,text ,reply_markup=START_BTN())
# if message is text
@dp.message_handler(filters.Text(startswith='Button'))
async def any_btn(message:Message):
    
    text = f"You chose {message.text} "
    await bot.send_message(message.chat.id,text,reply_markup=START_BTN())

   
# if message is contact

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)