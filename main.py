from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("👋 স্বাগতম OESBD Exchange Bot-এ!")

def main():
    updater = Updater("7892773671:AAEpnTvwxC8nPPUbSVIiJOV7u_WQnDtzw2o", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
