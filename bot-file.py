import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = '7234161687:AAHZDC3orXRLoiwTPs7CxwrPTVOqyKJOB7I'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Create inline keyboard with each button on a new line
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='PLAY SPACETAX', web_app=WebAppInfo(url='https://bettax.de'))],
    [InlineKeyboardButton(text='COMMUNITY', callback_data='button2')],
    [InlineKeyboardButton(text='SPIN IT!', url='https://www.x.me/spacetax.com')]
])
# Handle /start command
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # Image URL
    image_url = 'https://cdn.mos.cms.futurecdn.net/23zMEBA2esnXiuh7wjDj6c-650-80.jpg.webp'

    # Welcome text (caption)
    welcome_text = (
        "Welcome to SpaceTax: The Island Adventure Game 🏝️💰\n\n"
        "🌅 Welcome to SpaceTax, the addictive game where you can earn coins and attract visitors to your beautiful islands!\n\n"
        "🏝️ Gameplay Overview 🎰 In SpaceTax, your mission is to create and upgrade your very own islands, turning them into popular tourist destinations.\n\n"
        "💰 Earn Coins and Attract Visitors\n"
        " - Coin Collection: Collect coins as you play, which can be used to enhance your islands and facilities.\n"
        " - Visitor Experience: Attract more visitors by making your islands appealing and engaging!\n\n"
        "🌴 Upgrade Your Islands\n"
        "To maximize your visitor count, focus on upgrading essential features\n\n"
        "🎮 Addictive Gameplay\n"
        "SpaceTax offers an engaging and addictive gaming experience that keeps you coming back for more! Each upgrade you make enhances the appeal of your islands, leading to a steady influx of visitors."
    )

     # Send the image with the welcome text as a caption
    await bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=welcome_text, reply_markup=inline_kb)

# Handle button clicks
@dp.callback_query(lambda c: c.data == 'button2')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="You pressed the COMMUNITY button!")
    await bot.send_message(callback_query.from_user.id, "Join the SpaceTax community to stay updated!")

# Run the bot
async def main():
    # Start polling updates from Telegram
    await dp.start_polling(bot)

# Start the bot
if __name__ == '__main__':
    asyncio.run(main())
