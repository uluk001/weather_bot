import telebot
import requests
import json
import time


token='5173372970:AAHTgl74tjGImQeXp16nhV44tfX0jL23Qf4'
bot = telebot.TeleBot(token=token)
ff = time.ctime()
@bot.message_handler(commands=['start'])
def send_start(message):
    user = message.chat.first_name
    bot.send_message(message.chat.id, f"""Привет {user}, Я Синоптик-бот🌡️
Здесь ты можешь узнать погоду любой точки мира😉""")

@bot.message_handler(content_types='text')
def send_data(message):
    API_key = 'ca47be775bcdce04caa140c563a84b6d'
    city = message.text.title()
    API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'
    data = requests.get(API).json()
    coord = data['main']['temp']
    flike = data['main']['feels_like']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    if coord < 0:
        bot.send_message(message.chat.id, f"Температура в городе {city}:{coord}🌡️ \n Ощушается как:{flike} \n Минимальная температура:{min_temp}⏬ \n Максимальная температура:{max_temp}⏫ \n На улице холодно одевайся теплее не забудь шапку и шарф🧣🧥") 
    elif 0 > coord < 9:
         bot.send_message(message.chat.id, f"Температура в городе {city}:{coord}🌡️ \n Ощушается как:{flike} \n Минимальная температура:{min_temp}⏬ \n Максимальная температура:{max_temp}⏫ \n На улице и не жарко и не холодно одевайся соответственно🧣")
    elif coord > 9:
         bot.send_message(message.chat.id, f"Температура в городе {city}:{coord}🌡️ \n Ощушается как:{flike} \n Минимальная температура:{min_temp}⏬ \n Максимальная температура:{max_temp}⏫ \n На улице нормальная погода погуляем?🏕")
    elif coord > 25:
         bot.send_message(message.chat.id, f"Температура в городе {city}:{coord}🌡️ \n Ощушается как:{flike} \n Минимальная температура:{min_temp}⏬ \n Максимальная температура:{max_temp}⏫ \n На улице жарко гоу в басик?🧑‍🌾")
print('Бот работает...')
bot.infinity_polling()