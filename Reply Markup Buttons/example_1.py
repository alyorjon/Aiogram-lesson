from aiogram import Bot,Dispatcher,executor,filters,types
from config import BOT_TOKEN
from aiogram.types import Message,ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,ChatType
from aiogram.dispatcher.filters import Command,CommandStart,ChatTypeFilter

#Start bot
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)

def START_BTN():
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(KeyboardButton('Button 1'))
    button.add(KeyboardButton('Request contact',request_contact=True))
    button.add(KeyboardButton('Request location',request_location=True))
    return button

# Command start function
@dp.message_handler(filters.Command('start'),filters.ChatTypeFilter(ChatType.PRIVATE))
async def start_func_in_private(message:Message):
    text = "It is easy example for get contact and location"
    await bot.send_message(message.chat.id,text ,reply_markup=START_BTN())
# if message is text
@dp.message_handler(filters.Text(equals='Button 1'))
async def any_btn(message:Message):
    print("ishladi")
    text = "You chose Button 1 "
    await bot.send_message(message.chat.id,text,reply_markup=ReplyKeyboardRemove())

   
# if message is contact
@dp.message_handler(content_types=['contact'])
async def get_contact(message:types.Message):
    username = message.contact.full_name
    phone_number = message.contact.phone_number
    await bot.send_message(message.chat.id,f"Your username  is {username}.\n\nYour phone number is {phone_number}",reply_markup=ReplyKeyboardRemove())

# If message is location 
@dp.message_handler(content_types=['location'])
async def get_contact(message:types.Message):
    latitude = message.location.latitude
    longtitude = message.location.longitude
    place = message.location.live_period
    heading = message.location.heading

    await bot.send_message(message.chat.id,f"Your latitude is {latitude}.\n\nYour longtitude is {longtitude}\n\nYour live period is {place} \n\nHeading is {heading}",reply_markup=ReplyKeyboardRemove())
    await bot.send_location(message.chat.id,latitude=latitude,longitude=longtitude,live_period=place,heading=heading)



if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)