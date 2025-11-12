from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your bot token
BOT_TOKEN = "8533117794:AAE9Sj3-LGEofrhkf7u765SJDwspk6Q2pUY"

# Replace with your channel username (without the @)
CHANNEL_USERNAME = "jemawsecret"

confession_counter = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me your confession anonymously ✉️")

async def confess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global confession_counter
    message = update.message.text

    # Format and send the confession
    confession_text = f"💌 Confession #{confession_counter}:\n\n{message}"
    confession_counter += 1

    # Send to your channel
    await context.bot.send_message(chat_id=f"@{CHANNEL_USERNAME}", text=confession_text)

    await update.message.reply_text("✅ Your confession has been sent anonymously!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, confess))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
