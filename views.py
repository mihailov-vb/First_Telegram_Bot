# Тут будут написаны функции для логических вопросов.
import requests
import urllib.parse
from bs4 import BeautifulSoup
import feedparser
import sqlite3
import os
import random
from config import FEED_REM


# 1. Курс валют
def check_currency_USD():
# Ссылка на нужную страницу
    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=' \
                     'hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%' \
                     'D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131' \
                     'l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return f'Курс одного доллара: {convert[0].text} р.'
#print(check_currency_USD())


def check_currency_EUR():
# Ссылка на нужную страницу
    EUR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%BA%D1%83%D1' \
              '%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&aqs=chrome..69i57j35i39j0i433l3j0j0i131i433j0i433.4279j1j7&sourceid' \
              '=chrome&ie=UTF-8'

    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(EUR_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return f'Курс одного евро: {convert[0].text} р.'
#print(check_currency_EUR())


# 3. Статистика COVID (Аргументы:страна, город)
# Кол-во новых заболевших сегодня в СПб
def covid_spb_sick():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/coronavirus-saint-petersburg/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "rednum"})
    return convert[9].text
#covid_spb_sick()


# Кол-во выздровившихся сегодня в СПб
def covid_spb_recovered():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/coronavirus-saint-petersburg/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "greennum"})
    return convert[2].text

'''
def covid_spb_recovered():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/information/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll('th')
    print(convert)
covid_spb_recovered()'''


# Кол-во всего заболевших сегодня в СПб
def covid_spb_infected():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/coronavirus-saint-petersburg/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("th")
    roww = convert[22].text
    infected = roww.split('+')
    return infected[0]
#covid_spb_infected()


# Кол-во новых заболевших сегодня в Москве
def covid_msk_sick():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/coronavirus-saint-petersburg/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "rednum"})
    return convert[0].text
#covid_msk_sick()


# Кол-во выздровившихся сегодня в Москве
def covid_msk_recovered():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/coronavirus-saint-petersburg/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "greennum"})
    return convert[0].text
#covid_msk_recovered()


# Кол-во всего заболевших сегодня в России
def covid_msk_infected():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/coronavirus-saint-petersburg/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("th")
    roww = convert[8].text
    infected = roww.split('+')
    return infected[0]
#covid_msk_infected()


# Кол-во новых заболевших сегодня в России
def covid_rus_sick():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "rednum"})
    return convert[263].text
#covid_rus_sick()


# Кол-во выздровившихся сегодня в России
def covid_rus_recovered():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "greennum"})
    return convert[266].text
#covid_rus_recovered()


# Кол-во всего заболевших сегодня в Москве
def covid_rus_infected():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://coronavirus-control.ru/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("th")
    roww = convert[617].text
    infected = roww.split('+')
    return infected[0]
#covid_rus_infected()


# Кол-во новых заболевших сегодня в Мире
def covid_mir_sick():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://index.minfin.com.ua/reference/coronavirus/geography/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("small", {"class": "gold"})
    return convert[0].text
#covid_mir_sick()


# Кол-во выздровившихся сегодня в Мире
def covid_mir_recovered():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://index.minfin.com.ua/reference/coronavirus/geography/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("small", {"class": "green"})
    return convert[0].text
#covid_mir_recovered()


# Кол-во всего заболевших сегодня в Мире
def covid_mir_infected():
    # Ссылка на нужную страницу
    SICK_SPB = 'https://index.minfin.com.ua/reference/coronavirus/geography/'
    # Заголовки для передачи вместе с URL
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36'}
    # Парсим всю страницу
    full_page = requests.get(SICK_SPB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("td", {"align": "right"})
    return convert[0].text
#covid_mir_infected()


# 5. Выдача рейтинга фильма (аргумент: фильм)
#def kino_poisk():



# 6. Напоминание (аргумент: текст, дата, время)
# def reminders():
#     rem = feedparser.parse(FEED_REM)  # Скормил rss библиотеке
#     return f'{rem.entries[0].title}\n{rem.entries[0].link}\n\n{rem.entries[1].title}\n{rem.entries[1].link}\n\n' \
#            f'{rem.entries[2].title}\n{rem.entries[2].link}\n\n{rem.entries[3].title}\n{rem.entries[3].link}\n\n' \
#            f'{rem.entries[4].title}\n{rem.entries[4].link}'
# Функция заменена на более совершенную, см ниже с тем же именем


def reminders(): # Парсит feed и выводит заголовок, тело и ссылку
    date = []
    feed = feedparser.parse(FEED_REM)  # Скормил rss библиотеке
    for item_of_news in feed['items']:
        date.append(f'*{item_of_news["title"]}*')
#        date.append(item_of_news["description"])
        date.append(f'{item_of_news["link"]}\n➖➖➖➖➖➖➖➖➖➖➖\n')
    date_2 = '\n'.join(date)
    return date_2

# Счетчик новостей/заголовков (сколько новостей на данный момент)
def counter(dict):
    date = []
    feed = feedparser.parse(dict)
    for item_of_news in feed['items']:
        date.append(item_of_news["title"])
    count = len(date)
    return count
#print(counter(FEED_REM))


# Выдача рандомной картинки
def R():
    r = random.randint(1,54)
    return r



def ramdom_mot(dict_m):
    quote = dict_m[f'{random.randint(1,99)}']
    return quote


# Выдача погоды по запросу города
def weather(city):
    try:
        city_url = urllib.parse.quote(city)
        URL_WESTHER_2 = f'https://www.google.ru/search?newwindow=1&hl=ru&sxsrf=ALeKk03UW-imXVr9nrjMAUSnkJR6KLqWkg%3A1605' \
                        f'981749335&ei=NVa5X4zxE8j9rgSW3Kkw&q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+{city_url}&oq=' \
                        f'%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+{city_url}&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQRhCAAjIC' \
                        f'CAAyAggAMgIIADICCAAyAggAMgIIADICCAAyBwgAEBQQhwIyAggAOhEIABCwAxCKAxC3AxDlAhCLAzoFCAAQsQM6BAgAEA' \
                        f'06BggAEA0QHjoKCAAQCBANEAoQHjoICAAQBxAKEB46BwgAELEDEAo6BAgAEAo6CAgAELEDEIMBOgoIABCxAxAUEIcCUK7n' \
                        f'BVi7_gVg2oMGaAJwAHgBgAGrBYgBlw6SAQgxNS4xLjUtMZgBAKABAaoBB2d3cy13aXrIAQq4AQLAAQE&sclient=psy-ab' \
                        f'&ved=0ahUKEwjM37ydnJTtAhXIvosKHRZuCgYQ4dUDCA0&uact=5'
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/80.0.3987.149 Safari/537.36'}
        full_page = requests.get(URL_WESTHER_2, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert_city = soup.findAll("div", {"class": "wob_loc mfMhoc vk_gy vk_h"})  # город!
        convert_day_of_week = soup.findAll("div", {"class": "wob_dts vk_gy vk_sh"})  # день недели и время!
        convert_weather = soup.findAll("span", {"class": "vk_gy vk_sh"}) # погода!
        convert_precipitation = soup.findAll("span", {"id": "wob_pp"})   # осадки
        convert_humidity = soup.findAll("span", {"id": "wob_hm"})      # влажность
        convert_wind = soup.findAll("span", {"class": "wob_t", "id": "wob_ws"})     # ветер
        convert_t = soup.findAll("span", {"class": "wob_t TVtOme"}) # текущая температура!
        # print(convert_city[0].text) # город!
        # print(convert_day_of_week[0].text) # день недели и время!
        # print(convert_weather[0].text) # погода!
        # print(convert_precipitation[0].text) # вероятность осадков
        # print(convert_humidity[0].text) # влажность
        # print(convert_wind[0].text) # ветер
        # print(convert_t[0].text) # текущая температура!
        return f'По запросу: "*{city}*" найдена погода:\n\n🗺*{convert_city[0].text}*\n{convert_day_of_week[0].text}\n' \
               f'🌥{convert_weather[0].text}\n\n🌡Температура: {number_emoji(convert_t[0].text)} градуса\n\n' \
               f'☔Вероятность осадков: {number_emoji(convert_precipitation[0].text)}\n💧Влажность: ' \
               f'{number_emoji(convert_humidity[0].text)}\n🌬Скорость ветра: {number_emoji(convert_wind[0].text)}\n'
    except:
        return '*Ой, что то пошло не так.*\n\nЯ конечно мог поломаться 🤖, \nно всеже проверте Ваш запрос.\nОн должен ' \
               'начинаться в символа "@" и это обязательно!!!\n\n*Пример:*\n@Питер\n@ Москва\n@гаваи\n@ Варкута \n' \
               '_(можно и с ошибками писать, я Вас пойму!)_'
#print(weather('питер'))


#  Проверка и ВЫДАЧА ПОГОДЫ!!!!
def first(s):
    letters = list(s)
    if letters[0] == '@':
        request = s[1:]
        return weather(request)
    else:
        return '*Ой, что то пошло не так.*\n\nЯ конечно мог поломаться 🤖, \nно всеже проверте Ваш запрос.\nОн должен ' \
               'начинаться в символа "@" и это обязательно!!!\n\n*Пример:*\n@Питер\n@ Москва\n@гаваи\n@ Варкута \n' \
               '_(можно и с ошибками писать, я Вас пойму!)_'
#print(first('Питер'))



def number_emoji(my_str):
    emoji_dict = {'-': '❄',
                  '1': '1️⃣',
                  '2': '2️⃣',
                  '3': '3️⃣',
                  '4': '4️⃣',
                  '5': '5️⃣',
                  '6': '6️⃣',
                  '7': '7️⃣',
                  '8': '8️⃣',
                  '9': '9️⃣',
                  '0': '0️⃣'}
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in emoji_dict.items():
        my_str = my_str.replace(i, j)
    return my_str
#print(number_emoji('55'))