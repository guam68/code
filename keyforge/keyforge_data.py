import requests
import re
import json

page = '1'
url = 'https://www.keyforgegame.com/api/decks/?page=' + page +'&page_size=25&links=cards'

# Get the total number of decks and the number of pages required to process
response = requests.get(url).json()
s = '\'count\': \d+'
count = (re.findall(s, str(response))[0].split(':')[1]).strip()
pages = int(count) // 25


card_list = []
# cards = response['_linked']['cards']
   
for i in range(-(-int(pages)//25)):
    
    url = 'https://www.keyforgegame.com/api/decks/?page=' + page +'&page_size=25&links=cards'
    data = requests.get(url).json()
    cards = data['_linked']['cards']

    for i, card in enumerate(cards):
        if card not in card_list:
            card_list.append(card)

    page = str(int(page) + 1)

print(len(card_list))

with open('card_list.txt', 'w', encoding='utf-8') as file:
    file.write(str(card_list))