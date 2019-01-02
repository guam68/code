import requests
import re
import json
import time
from time import sleep
import ast

start_time = time.time()
page = '1'
site = ('https://www.keyforgegame.com/api/decks/?page=','&page_size=25&links=cards&ordering=date')

# Get the number of pages required to process
def get_num_pages(url, count_file):
    response = requests.get(url).json()
    count = int(response['count'])
    
    with open(count_file, 'r', encoding='utf-8') as file:
        old_count = file.readline()

    new_count = count - int(old_count)
    pages = -(-new_count // 25)
    print(f'count: {count}\noldcount: {old_count}pages: {pages}')
    return pages, count


def get_unique_cards(page, site):
    url = site[0] + page + site[1]
    with open('card_list2.txt', 'r', encoding='utf-8') as file:
        file.readline()
        card_list = ast.literal_eval(file.read())

    num_pages, deck_count = get_num_pages(url, 'card_list2.txt')
    
    for i in range(num_pages):
        url = site[0] + page + site[1]
        try:
            data = requests.get(url).json()
            cards = data['_linked']['cards']

            for card in cards:
                if card not in card_list:
                    card_list.append(card)

            print(page, '/', num_pages)
            page = str(int(page) + 1)
            sleep(.5)
        except:
            with open('card_list2.txt', 'w', encoding='utf-8') as file:
                file.write(f'Fail on page {page}\n')
                file.write(str(card_list))
            quit()
        

    print(len(card_list))

    with open('card_list2.txt', 'w', encoding='utf-8') as file:
        file.write(str(deck_count) + '\n')
        file.write(str(card_list))


def get_decks(page, site):
    url = site[0] + page + site[1]

    with open('deck_list.txt', 'r', encoding='utf-8') as file:
        file.readline()
        deck_list = ast.literal_eval(file.read())

    num_pages, deck_count = get_num_pages(url, 'deck_list.txt')

    for i in range(num_pages):
        try:
            url = site[0] + page + site[1]
            data = requests.get(url).json()
            decks = data['data']

            for deck in decks:
                if deck not in deck_list:
                    deck_list.append(deck)

            print(page, '/', num_pages)
            page = str(int(page) + 1)
            sleep(.5)
        except:
            with open('deck_list.txt', 'w', encoding='utf-8') as file:
                file.write(f'Failed on page {page}\n')
                file.write(str(deck_list))
            quit()
    
    print(len(deck_list))

    with open('deck_list.txt', 'w', encoding='utf-8') as file:
        file.write(str(deck_count) + '\n')
        file.write(str(deck_list))





# get_unique_cards(page, site)
# # get_decks(page, site)

elapsed = int(time.time() - start_time)
if elapsed/60/60 > 1:
    print(f'Run Time: {elapsed//3600} hours and {int(elapsed%3600/60)} minutes')
elif elapsed / 60 > 1:
    print(f'Run Time: {elapsed//60} minutes and {int(elapsed%60)} seconds')
else:
    print(f'Run Time: {elapsed} seconds')

