import telebot

from config import TG_TOKEN, users, FEED_REM
from keyboard import keyboard1, keyboard2, keyboard3, keyboard4, keyboard6, keyboard7, keyboard8, keyboard9, keyboard10
from models import DATA_RUOTE
from rss import horoscope_d, horoscope_w, horoscope_m
from stickers import sticker_1, sticker_2, sticker_3, sticker_5
from text import info, info_2, hello, hello_2, covid_memu, weather_text, error
from views import check_currency_EUR, check_currency_USD, covid_spb_sick, covid_spb_recovered, covid_spb_infected, \
    covid_msk_sick, covid_msk_recovered, covid_msk_infected, covid_rus_sick, covid_rus_recovered, covid_rus_infected, \
    covid_mir_sick, covid_mir_recovered, covid_mir_infected, reminders, counter, ramdom_mot, R, first

bot = telebot.TeleBot(TG_TOKEN)


# Проверка, открыт ли доступ в пользовании ботом для пользователя и чата.
@bot.message_handler(func=lambda message: message.chat.id not in users)
def some(message):
   bot.send_message(message.chat.id, "Извините, у Вас нет доступа к Боту!\n\nОбратитесь по адресу mvb.goszak@gmail.com")
   bot.send_sticker(message.chat.id, sticker_5)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Расскажи, что ты умееш!": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Расскажи, что ты умееш!!!')
    elif call.data == "Не надо, я и так все знаю!":
        bot.send_message(call.message.chat.id, 'Не надо, я и так все знаю!')

# Выводит информацию по команде
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}!\nЯ стартанул!!! 🤖\nРассказать что я умею?\n\n'
                                      'Но для начала, отправь мне стикер😇', reply_markup=keyboard1)




@bot.message_handler(commands=['menu'])
def start_message(message):
    bot.send_message(message.chat.id, info_2)




@bot.message_handler(commands=['rub_eur_usd'])
def start_message(message):
    bot.send_message(message.chat.id, f'Итак, что мы видим🔎💹\n\n{check_currency_EUR()}\n{check_currency_USD()}\n\n'
                                      f'Пора бы уже ЗП в валюте получать...', reply_markup=keyboard4)
    bot.send_sticker(message.chat.id, sticker_3)




@bot.message_handler(commands=['covid_19'])
def start_message(message):
    bot.send_message(message.chat.id, covid_memu, reply_markup=keyboard4)


@bot.message_handler(commands=['covid_spb'])
def start_message(message):
    bot.send_message(message.chat.id, f'*В Санкт-Петербурге сегодня:*\n'
                                      f'🔹_{covid_spb_sick()}_ новых случаев заболевания короновирусной инфекцией.\n'
                                      f'🔹_{covid_spb_recovered()}_ человек выздровило от короновирусной инфекцией.\n'
                                      f'🔹_{covid_spb_infected()}_ человек заражено короновирусной инфекцией.\n\n🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠\n\n'
                                      f'Будьте аккуратнее и берегите ближних.', reply_markup=keyboard3, parse_mode='Markdown')


@bot.message_handler(commands=['covid_msk'])
def start_message(message):
    bot.send_message(message.chat.id, f'*В Москве сегодня:*\n'
                                      f'🔹_{covid_msk_sick()}_ новых случаев заболевания короновирусной инфекцией.\n'
                                      f'🔹_{covid_msk_recovered()}_ человек выздровило от короновирусной инфекцией.\n'
                                      f'🔹_{covid_msk_infected()}_ человек заражено короновирусной инфекцией.\n\n🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠\n\n'
                                      f'Будьте аккуратнее и берегите ближних.', reply_markup=keyboard3, parse_mode='Markdown')


@bot.message_handler(commands=['covid_rus'])
def start_message(message):
    bot.send_message(message.chat.id, f'*В России сегодня:*\n'
                                      f'🔹_{covid_rus_sick()}_ новых случаев заболевания короновирусной инфекцией.\n'
                                      f'🔹_{covid_rus_recovered()}_ человек выздровило от короновирусной инфекцией.\n'
                                      f'🔹_{covid_rus_infected()}_ человек заражено короновирусной инфекцией.\n\n🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠\n\n'
                                      f'Будьте аккуратнее и берегите ближних.', reply_markup=keyboard3, parse_mode='Markdown')


@bot.message_handler(commands=['covid_mir'])
def start_message(message):
    bot.send_message(message.chat.id, f'*В Мире сегодня:*\n'
                                      f'🔹_{covid_mir_sick()}_ новых случаев заболевания короновирусной инфекцией.\n'
                                      f'🔹_{covid_mir_recovered()}_ человек выздровило от короновирусной инфекцией.\n'
                                      f'🔹_{covid_mir_infected()}_ человек заражено короновирусной инфекцией.\n\n🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠\n\n'
                                      f'Будьте аккуратнее и берегите ближних.', reply_markup=keyboard3, parse_mode='Markdown')




@bot.message_handler(commands=['history'])
def start_message(message):
    bot.send_message(message.chat.id, f'*У меня для Вас {counter(FEED_REM)} исторических событий которые произошли '
                                      f'сегодня:*\n⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛\n\n'
                                      f'{reminders()}', reply_markup=keyboard4, parse_mode='Markdown')



# Запуск гороскопа
@bot.message_handler(commands=['horoscope'])
def start_message(message):
    bot.send_message(message.chat.id, f'*Выбери период на который хочеш узнать гороскоп*\n🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮\n\n',
                     reply_markup=keyboard6, parse_mode='Markdown')




# Запуск мотиватора. Вывод цитаты и картинки
@bot.message_handler(commands=['motivator'])
def start_message(message):
    bot.send_message(message.chat.id, f'🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁')
#    bot.send_photo(message.chat.id, open(fr'C:\Users\MVB\PycharmProjects\bot_1\image\({R()}).jpg', 'rb'))
    bot.send_photo(message.chat.id, open(fr'.image\({R()}).jpg', 'rb'))
    bot.send_message(message.chat.id, f'🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁\n\n{ramdom_mot(DATA_RUOTE)}\n\n🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁',
                     reply_markup=keyboard4)


# Выдача информации о погоде
@bot.message_handler(commands=['weather'])
def start_message(message):
    bot.send_message(message.chat.id, weather_text, reply_markup=keyboard4, parse_mode='Markdown')



# Меню и навигация по гороскопу
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'гороскоп на день':
        bot.send_message(message.chat.id, 'Теперь выбери знак задиака\n\n♈♉♊♋♌♍♎♏♐♑♒♓', reply_markup=keyboard7)
    elif message.text.lower() == 'гороскоп на неделю':
        bot.send_message(message.chat.id, 'Теперь выбери знак задиака\n\n♈♉♊♋♌♍♎♏♐♑♒♓', reply_markup=keyboard8)
    elif message.text.lower() == 'гороскоп на месяц':
        bot.send_message(message.chat.id, 'Теперь выбери знак задиака\n\n♈♉♊♋♌♍♎♏♐♑♒♓', reply_markup=keyboard9)
    elif message.text.lower() == '⬆ вернуться к выбору периода':
        bot.send_message(message.chat.id, f'*Выбери период на который хочеш узнать гороскоп🔮*\n\n\n',
                     reply_markup=keyboard6, parse_mode='Markdown')

    elif message.text.lower() == '♈ овен':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(1)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♉ телец':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(2)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♊ близнецы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(3)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♋ рак':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(4)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♌ лев':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(5)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♍ дева':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(6)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♎ весы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(7)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♏ скорпион':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(8)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♐ стрелец':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(9)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♑ козерог':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(10)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♒ водолей':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(11)}', reply_markup=keyboard7, parse_mode='Markdown')
    elif message.text.lower() == '♓ рыбы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на сегодня🔮\n\n{horoscope_d(12)}', reply_markup=keyboard7, parse_mode='Markdown')

    elif message.text.lower() == '♈  овен':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(0)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♉  телец':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(1)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♊  близнецы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(2)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♋  рак':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(3)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♌  лев':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(4)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♍  дева':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(5)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♎  весы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(6)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♏  скорпион':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(7)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♐  стрелец':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(8)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♑  козерог':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(9)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♒  водолей':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(10)}', reply_markup=keyboard8, parse_mode='Markdown')
    elif message.text.lower() == '♓  рыбы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на неделю🔮\n\n{horoscope_w(11)}', reply_markup=keyboard8, parse_mode='Markdown')

    elif message.text.lower() == '♈   овен':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(0)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♉   телец':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(1)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♊   близнецы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(2)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♋   рак':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(3)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♌   лев':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(4)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♍   дева':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(5)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♎   весы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(6)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♏   скорпион':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(7)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♐   стрелец':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(8)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♑   козерог':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(9)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♒   водолей':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(10)}', reply_markup=keyboard9, parse_mode='Markdown')
    elif message.text.lower() == '♓   рыбы':
        bot.send_message(message.chat.id, f'🔮Гороскоп на месяц🔮\n\n{horoscope_m(11)}', reply_markup=keyboard9, parse_mode='Markdown')

    elif message.text.lower() == '1. 📈📉курсы валют usd и eur':
        bot.send_message(message.chat.id, f'Итак, что мы видим🔎💹\n\n{check_currency_EUR()}\n{check_currency_USD()}\n\n'
                                      f'Пора бы уже ЗП в валюте получать...', reply_markup=keyboard4)
        bot.send_sticker(message.chat.id, sticker_3)
    elif message.text.lower() == '2. 🌡погода':
        bot.send_message(message.chat.id, weather_text, reply_markup=keyboard4, parse_mode='Markdown')
    elif message.text.lower() == '3. 🤥covid-19':
        bot.send_message(message.chat.id, covid_memu, reply_markup=keyboard4)
    elif message.text.lower() == '4. 🏁мотиватр':
        bot.send_message(message.chat.id, f'🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁')
        bot.send_photo(message.chat.id, open(fr'C:\Users\MVB\PycharmProjects\bot_1\image\({R()}).jpg', 'rb'))
        bot.send_message(message.chat.id,
                         f'🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁\n\n{ramdom_mot(DATA_RUOTE)}\n\n🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁',
                         reply_markup=keyboard4)
    elif message.text.lower() == '5. 🕰событие':
        bot.send_message(message.chat.id, f'*У меня для Вас {counter(FEED_REM)} исторических событий которые произошли '
                                          f'сегодня:*\n⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛⌛\n\n'
                                          f'{reminders()}', reply_markup=keyboard4, parse_mode='Markdown')
    elif message.text.lower() == '6. 🎬рейтинг на кинопоиск':
        bot.send_message(message.chat.id, error, reply_markup=keyboard4) # Тут текст о недоделанном коде
        bot.send_sticker(message.chat.id, sticker_2) # К сообщению прикрепляет стикер
    elif message.text.lower() == '7. 🔔напоминание':
        bot.send_message(message.chat.id, error, reply_markup=keyboard4) # Тут текст о недоделанном коде
        bot.send_sticker(message.chat.id, sticker_2) # К сообщению прикрепляет стикер
    elif message.text.lower() == '8. 🔮гороскоп':
        bot.send_message(message.chat.id,
                         f'*Выбери период на который хочеш узнать гороскоп*\n🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮\n\n',
                         reply_markup=keyboard6, parse_mode='Markdown')
    elif message.text.lower() == '🔂 перезапустить бота':
        bot.send_message(message.chat.id, f'Для перезагрузки введи(нажми) команду /start')

    elif message.text.lower() == 'расскажи, что ты умееш!':
        bot.send_message(message.chat.id, info, reply_markup=keyboard2)
        # Тут ссылка на большой текст, + вывод клавиатуры
    elif message.text.lower() == 'не надо, я и так все знаю!':
        bot.send_message(message.chat.id, info_2, reply_markup=keyboard10) # Тут ссылка на большой текст
    elif message.text.lower() == 'поехали, попробуем!':
        bot.send_message(message.chat.id, info_2, reply_markup=keyboard10) # Тут ссылка на большой текст
    elif message.text.lower() == '⬆ вернуться в меню':
        bot.send_message(message.chat.id, info_2, reply_markup=keyboard10) # Тут ссылка на большой текст
    elif message.text.lower() == '⬆ вернуться в выбор региона':
        bot.send_message(message.chat.id, covid_memu, reply_markup=keyboard4) # Тут ссылка на большой текст
    elif hello in message.text.lower(): # Если в запросе есть определенный текст, то выводить...
        bot.reply_to(message, 'И тебе привет добрый друг!')
    elif hello_2 in message.text.lower(): # Если в запросе есть определенный текст, то выводить...
        bot.reply_to(message, 'Оооо, дела идут неплохо, обрастаю знаниями по чуть чуть\n🙂🙃')
    elif '@' in message.text.lower(): # Если в запросе есть определенный текст, то выводить...
        bot.send_message(message.chat.id, first(message.text), reply_markup=keyboard4, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, error, reply_markup=keyboard4) # Тут текст о недоделанном коде
        bot.send_sticker(message.chat.id, sticker_2) # К сообщению прикрепляет стикер


# Реагирует на стикиры
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    bot.reply_to(message, 'Мне тоже нравятся стикеры))')
    bot.send_sticker(message.chat.id, sticker_1)



bot.polling(none_stop=True, interval=1)



# while True:
#     try:
#         bot.polling(none_stop=True)
#
#     except Exception as e:
#         print(e)
#
#         time.sleep(15)
