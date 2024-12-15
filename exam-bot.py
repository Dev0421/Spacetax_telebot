from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN' with your actual Telegram bot token
TOKEN = '7741562616:AAEmXdTTcCkZAqe3zfrXSkZdgDYbQJgjNIc'
IMAGE_URL = 'https://example.com/path/to/your/image.jpg'  # Replace with your image URL

def start(update: Update, context: CallbackContext) -> None:
    # Send the image
    update.message.reply_photo(photo=IMAGE_URL)

    # Send the welcome message
    welcome_text = (
        "Welcome to Boinkers: Parody Game 💩💎\n\n"
        "🤪 Chase the stupid dream of getting to the moon by farming the ultimate game memecoin, $BOINK.\n\n"
        "▪️ Free2Play 🔥 Jump into meme chaos, where humor has no limits.\n\n"
        "▪️ Slut Machine 🎰 Spin and you might win the ultimate jackpot, but beware of bears!\n\n"
        "▪️ Launch 💎 $BOINK will launch on TON!\n\n"
        "▪️ Drop 🪂 Collect as much shitcoins as points for the upcoming $BOINK drop."
    )
    
    update.message.reply_text(welcome_text)

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()