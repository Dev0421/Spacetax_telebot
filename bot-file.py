import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = '7234161687:AAHZDC3orXRLoiwTPs7CxwrPTVOqyKJOB7I'
BACKEND_API = 'https://bettax.de/api'
# BACKEND_API = 'http://104.223.97.2:8081/api'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Create inline keyboard with each button on a new line
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='PLAY SPACETAX', web_app=WebAppInfo(url='https://bettax.de'))],
    [InlineKeyboardButton(text='COMMUNITY', callback_data='button2')],
    [InlineKeyboardButton(text='SPIN IT!', url='https://www.x.me/spacetax.com')]
])

########################### FUNCTIONS ################################
def send_user_data(user_data):
    try:
        print(user_data)  # For debugging purposes
        response = requests.post(f"{BACKEND_API}/user/validate", json=user_data)
        response.raise_for_status()  # Raise an HTTPError for bad HTTP responses
        try:
            print(response.status_code, response.json())  # Attempt to parse JSON
        except ValueError:
            print(f"Response is not JSON: {response.text}")
    except requests.RequestException as e:
        print(f"Failed to send user data: {e}")

############### HANDLERS ####################

# Handle /start command
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    try:
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

        user_data = {
            "userId": message.from_user.id,
            "firstName": message.from_user.first_name,
            "lastName": message.from_user.last_name or "",
            "username": message.from_user.username or "",
            "languageCode": message.from_user.language_code
        }
        await message.reply(
            f"Hello {user_data['firstName']} {user_data['lastName']}!\n"
            f"Your ID: {user_data['userId']}\n"
            f"Username: @{user_data['username']}\n"
            f"Language: {user_data['languageCode']}"
        )
        # Send data to backend
        send_user_data(user_data)
    except Exception as e:
        print(f"Error in send_welcome: {e}")


# Handle button clicks
@dp.callback_query(lambda c: c.data == 'button2')
async def process_callback(callback_query: types.CallbackQuery):
    try:
        await bot.answer_callback_query(callback_query.id, text="You pressed the COMMUNITY button!")
        await bot.send_message(callback_query.from_user.id, "Join the SpaceTax community to stay updated!")
    except Exception as e:
        print(f"Error in process_callback: {e}")

########################### RUN THE BOT ################################

async def main():
    try:
        print("Bot is starting...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error in main(): {e}")


if __name__ == "__main__":
    # For Windows compatibility
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
