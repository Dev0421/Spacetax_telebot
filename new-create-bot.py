import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.filters import Command

API_TOKEN = '7741562616:AAEmXdTTcCkZAqe3zfrXSkZdgDYbQJgjNIc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Inline keyboard
inline_kb = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text='PLAY SPACETAX', web_app={'url': 'https://c965-104-223-97-2.ngrok-free.app/'})
btn2 = InlineKeyboardButton(text='COMMUNITY', callback_data='button2')
btn3 = InlineKeyboardButton(text='SPIN IT!', url='https://www.x.me/spacetax.com')
inline_kb.add(btn1, btn2, btn3)

@dp.message(Command('start'))
async def send_welcome(message: Message):
    image_url = 'https://www.premiumbeat.com/blog/wp-content/uploads/2021/03/Excited-Male-Gamer-1.jpg'
    welcome_text = (
        "Welcome to SpaceTax: The Island Adventure Game 🏝️💰\n\n"
        "🌅 Welcome to SpaceTax, the addictive game where you can earn coins and attract visitors to your beautiful islands!\n\n"
        "🏝️ Gameplay Overview 🎰..."
    )
    await message.answer_photo(photo=image_url, caption=welcome_text, reply_markup=inline_kb)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
