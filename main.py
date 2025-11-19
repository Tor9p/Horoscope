import requests
from bs4 import BeautifulSoup


url = "https://dzen.ru/topic/horoscope"

# znak_zodiak = [oven, telec, bliznec, rak, lev, deva, vesy, scorpion, strelec, kozerog, vodoley, ryby]

# znak_zodiak = {
#     'овен': 'oven',
#     'телец': 'telec', 
#     'близнецы': 'bliznec',
#     'рак': 'rak',
#     'лев': 'lev',
#     'дева': 'deva',
#     'весы': 'vesy',
#     'скорпион': 'scorpion',
#     'стрелец': 'strelec',
#     'козерог': 'kozerog',
#     'водолей': 'vodoley',
#     'рыбы': 'ryby'
# }

# znak = input("Введите ваш знак зодиака: ").lower()

# if znak in znak_zodiak:
# 	print(znak_zodiak[znak])

# else:
# 	print('Такой знак зодиака не найден')


response = requests.get(url)

print("---------\n", response, '\n---------')

bs = BeautifulSoup(response.text, "lxml")
# print(bs)

temp = bs.find('span', 'topic-channel--rich-text__text-24')
print(temp.text)

