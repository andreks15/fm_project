import telebot

import requests
import random

TOKEN = '5621435770:AAFWtY-f2V7K0a2M_XSLNw1djnKbX63KjMw'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, любитель щенят!")
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Анекдот")
    item2 = telebot.types.KeyboardButton("Собака")
    item3 = telebot.types.KeyboardButton("Человек")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Человек':
        img_data = requests.get('https://thispersondoesnotexist.com/image').content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)
        with open('image_name.jpg', 'rb') as handler:
            bot.send_photo(message.chat.id, photo=handler)
    elif message.text == 'Анекдот':
        try:
            a = random.randint(-1, 2)
            if a < 1:
                response = requests.get('https://v2.jokeapi.dev/joke/Dark')
            else:
                response = requests.get('https://v2.jokeapi.dev/joke/Programming')
            anec = response.json()['joke']
            bot.send_message(message.chat.id, 'Вот ржака')
            bot.send_message(message.chat.id, anec)
        except:
            bot.send_message(message.chat.id, 'не получилось((( \n попробуй еще раз')
    elif message.text == 'Собака':
        image_url = ''
        while True:
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            response_status = response.json()['status']
            if response_status == 'success':
                image_url = response.json()['message']
                break
        bot.send_message(message.chat.id, 'Вот твой песель')
        bot.send_photo(message.chat.id, image_url)


bot.infinity_polling()
