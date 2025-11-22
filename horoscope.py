import requests
from bs4 import BeautifulSoup


url = "https://dzen.ru/topic/horoscope"


znak_zodiak = {
    'овен': 'oven',
    'телец': 'telec', 
    'близнецы': 'bliznec',
    'рак': 'rak',
    'лев': 'lev',
    'дева': 'deva',
    'весы': 'vesy',
    'скорпион': 'skorpion',
    'стрелец': 'strelec',
    'козерог': 'kozerog',
    'водолей': 'vodoley',
    'рыбы': 'ryby'
}


def get_horo():
    # znak = input("Введите ваш знак зодиака: ").lower()
    znak = 'овен'
    if znak in znak_zodiak:
        try:
            url = '-'.join([url, znak_zodiak[znak]])
            #отладка
            print(url)
            print("------------")
            
            response = requests.get(url) 
            bs = BeautifulSoup(response.text, "lxml")
            base = bs.find('span', 'topic-channel--rich-text__text-24')

            print(base.text)
        except:
            pass
    else:
          print('Такой знак зодиака не найден')