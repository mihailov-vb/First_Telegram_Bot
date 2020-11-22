import feedparser
from config import FEED_HORO_D, FEED_HORO_M, FEED_HORO_W




# Гороскоп на день (первый знак начинается с нуля '1')
def horoscope_d(i):
    horo = []
    feed = feedparser.parse(FEED_HORO_D)
    horo.append(f'*{feed.entries[i].title}*')
    horo.append(f'{feed.entries[i].description}')
    horo_2 = '\n'.join(horo)
    return horo_2


# Гороскоп на неделю (первый знак начинается с нуля '0')
def horoscope_w(i):
    horo = []
    feed = feedparser.parse(FEED_HORO_W)
    horo.append(f'*{feed.entries[i].title}*')
    horo.append(f'{feed.entries[i].description}')
    horo_2 = '\n'.join(horo)
    return horo_2


# Гороскоп на месяц (первый знак начинается с нуля '0')
def horoscope_m(i):
    horo = []
    feed = feedparser.parse(FEED_HORO_M)
    horo.append(f'*{feed.entries[i].title}*')
    horo.append(f'{feed.entries[i].description}')
    horo_2 = '\n'.join(horo)
    return horo_2


# print(horoscope_d(1))
# print(horoscope_w(0))
# print(horoscope_m(0))