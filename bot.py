import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from logic import Text2ImageAPI
from config import API_TOKEN_tg, API_KEY, SECRET_KEY

bot = telebot.TeleBot(API_TOKEN_tg)


def main_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Промпты', callback_data='prompts'),
               InlineKeyboardButton('Включить авто-отправку', callback_data='auto-send'))

    return markup

def prompts_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Добавить промпты', callback_data='prompt-add'),
               InlineKeyboardButton('Удалить промпты', callback_data='prompt-delete'),
               InlineKeyboardButton('Назад', callback_data='pm_cancel'))

    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот, который присылает тебе картинку котика каждое утро.\n", reply_markup=main_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    #                                       main_markup
    if call.data == "prompts":
        bot.send_message('Ты выбрал: Промпты\nВыбери действие:')

    elif call.data == "auto-send":
        bot.send_message(call.message.chat.id, obj.translation)

    #                                       prompts_markup
    if call.data == "prompt-add":
        bot.send_message('Ты выбрал: Промпты\nВыбери действие:')

    elif call.data == "prompt-delete":
        bot.send_message(call.message.chat.id, obj.translation)

    elif call.data == "pm_cancel":
        bot.send_message("Привет! Я бот, который присылает тебе картинку котика каждое утро.\n", reply_markup=main_markup())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "Я получил твое сообщение! Что ты хочешь с ним сделать?",
    reply_markup=main_markup())


bot.infinity_polling(none_stop=True)