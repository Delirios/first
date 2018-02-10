import telebot

TOKEN = '538973717:AAEKe_3tleaZrzSvBO3nwgCv_HUDVq74nyY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я Dimas!')

@bot.message_handler(commands=['kyky'])
def send_stupid_men(message):
    msg = bot.send_message(message.chat.id, 'Ти не чуєш я Dimas!')

bot.polling()

