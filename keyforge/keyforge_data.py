import requests
import re
import json
import time
from time import sleep
import ast

start_time = time.time()
page = '1'
url = 'https://www.keyforgegame.com/api/decks/?page=' + page +'&page_size=25&links=cards&ordering=-date'

# Get the number of pages required to process
def get_num_pages(url):
    response = requests.get(url).json()
    s = '\'count\': \d+'
    count = int((re.findall(s, str(response))[0].split(':')[1]).strip())
    
    with open('card_list2.txt', 'r', encoding='utf-8') as file:
        old_count = file.readline()

    new_count = count - int(old_count)
    pages = -(-new_count // 25)
    return pages, count


def get_unique_cards(page, url):
    with open('card_list2.txt', 'r', encoding='UTF-8') as file:
        file.readline()
        card_list = ast.literal_eval(file.read())

    num_pages, deck_count = get_num_pages(url)
    
    for i in range(num_pages):
        
        data = requests.get(url).json()
        cards = data['_linked']['cards']

        for card in cards:
            if card not in card_list:
                card_list.append(card)

        print(page, '/', num_pages)
        page = str(int(page) + 1)
        sleep(1)
        

    print(len(card_list))

    with open('card_list2.txt', 'w', encoding='utf-8') as file:
        file.write(str(deck_count) + '\n')
        file.write(str(card_list))


def get_decks():
    deck_list = []
    s = '\"data\":(.*?),\"_linked\"'
    deck_list += re.findall(s, )


get_unique_cards(page, url)

print('Run Time: ', time.time() - start_time)

