import telebot
from telebot.types import ReplyKeyboardMarkup

keyboard1: ReplyKeyboardMarkup = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Расскажи, что ты умееш!')
keyboard1.row('Не надо, я и так все знаю!')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Поехали, попробуем!')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('⬆ Вернуться в выбор региона')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('⬆ Вернуться в меню')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('/covid_spb')
keyboard5.row('/covid_msk')
keyboard5.row('/covid_rus')
keyboard5.row('/covid_mir')

keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('Гороскоп на день')
keyboard6.row('Гороскоп на неделю')
keyboard6.row('Гороскоп на месяц')
keyboard6.row('⬆ Вернуться в меню')

keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row('♈ Овен', '♉ телец')
keyboard7.row('♊ Близнецы', '♋ Рак')
keyboard7.row('♌ Лев', '♍ Дева')
keyboard7.row('♎ Весы', '♏ Скорпион')
keyboard7.row('♐ Стрелец', '♑ Козерог')
keyboard7.row('♒ Водолей', '♓ Рыбы')
keyboard7.row('⬆ Вернуться к выбору периода')

keyboard8 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard8.row('♈  Овен', '♉  Телец')
keyboard8.row('♊  Близнецы', '♋  Рак')
keyboard8.row('♌  Лев', '♍  Дева')
keyboard8.row('♎  Весы', '♏  Скорпион')
keyboard8.row('♐  Стрелец', '♑  Козерог')
keyboard8.row('♒  Водолей', '♓  Рыбы')
keyboard8.row('⬆ Вернуться к выбору периода')

keyboard9 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard9.row('♈   Овен', '♉   Телец')
keyboard9.row('♊   Близнецы', '♋   Рак')
keyboard9.row('♌   Лев', '♍   Дева')
keyboard9.row('♎   Весы', '♏   Скорпион')
keyboard9.row('♐   Стрелец', '♑   Козерог')
keyboard9.row('♒   Водолей', '♓   Рыбы')
keyboard9.row('⬆ Вернуться к выбору периода')

keyboard10 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard10.row('1. 📈📉Курсы валют USD и EUR')
keyboard10.row('2. 🌡Погода', '3. 🤥COVID-19')
keyboard10.row('4. 🏁Мотиватр', '5. 🕰Событие')
keyboard10.row('6. 🎬Рейтинг на КиноПоиск')
keyboard10.row('7. 🔔Напоминание', '8. 🔮Гороскоп')
keyboard10.row('🔂 Перезапустить бота')