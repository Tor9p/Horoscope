import requests
from bs4 import BeautifulSoup

base_url = "https://dzen.ru/topic/horoscope"

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


def get_horo(znak):
    if znak in znak_zodiak:
        try:
            url = f"{base_url}-{znak_zodiak[znak]}"
            
            # отладка
            print(f"запрос к url: {url}")
            print("------------")
            
            response = requests.get(url) 
            # response.raise_for_status()

            bs = BeautifulSoup(response.text, "lxml")
            
            base = bs.find('span', 'topic-channel--rich-text__text-24')
            
            otvet = base.text
            print(otvet)
            return otvet

        except AttributeError:
            return "Не удалось распарсить страничку..."
    else:
        return 'Такой знак зодиака не найден'

# get_horo("рак")