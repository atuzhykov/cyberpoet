import poemgenerator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='637268565:AAFsFA5Z7LaohhqlVbL10MM_DAAgVtP5o8A') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привіт, Оксана Чміль, натисни щось')
def textMessage(bot, update):
    response = poemgenerator.generate('Andrukhovych.txt')
    bot.send_message(chat_id=update.message.chat_id, text=response)
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()