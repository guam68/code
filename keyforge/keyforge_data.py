# 2266 uniques and 443724 decks recorded

import requests
import re
import json
import time
from time import sleep
import ast

program_start_time = time.time()

page = '1' # 33725 fail pg7625 fail 443724
site = ('https://www.keyforgegame.com/api/decks/?page=','&page_size=25&links=cards&ordering=-date') # Date should be negative after initial data collection

# Get the number of pages required to process
def get_num_pages(url, count_file):
    response = requests.get(url).json()
    count = int(response['count'])
    
    with open(count_file, 'r', encoding='utf-8') as file:
        old_count = file.readline()

    new_count = count - int(old_count)
    pages = -(-new_count // 25)
    print(f'count: {count}\noldcount: {old_count}\npages: {pages}')
    return pages, count


def get_unique_cards(page, site):
    url = site[0] + page + site[1]
    error_flag = 0
    with open('card_list.txt', 'r', encoding='utf-8') as file:
        file.readline()
        card_list = ast.literal_eval(file.read())

    num_pages, deck_count = get_num_pages(url, 'card_list.txt')
    
    for i in range(num_pages):
        start_time = time.time()
        url = site[0] + page + site[1]

        try:
            data = requests.get(url).json()
            cards = data['_linked']['cards']
        except:
            error_flag += 1
            print('SSLError timeout. Sleeeeeep')
            sleep(5)
            print('Program resumed')
            continue


        for card in cards:      # Added after base cards have been collected. Will need to be modified for new sets. Speeds up collection
            if card['is_maverick']:
                if card in card_list:
                    print(card)
                else:
                    card_list.append(card)
                    print('card added')

        print(page, '/', num_pages, ' ', end='')
        page = str(int(page) + 1)
        print('Page process time: ', int(time.time() - start_time))

        with open('card_list.txt', 'w', encoding='utf-8') as file:
            file.write(str(deck_count) + '\n')
            file.write(str(card_list))    
        
        sleep(.5)
        

    print(len(card_list))
    print(error_flag)

    
def get_decks(page, site):
    url = site[0] + page + site[1]
    num_pages, deck_count = get_num_pages(url, 'deck_count.txt')

    print('\nReading from vault...')
    with open('deck_list.txt', 'r', encoding='utf-8') as file:
        file.readline()
        master_vault = ast.literal_eval(file.read())
    print('Vault copied! Starting data download.\n')

    counter = 0
    for i in range(num_pages):
        start_time = time.time()
        url = site[0] + page + site[1]

        data = requests.get(url).json()
        decks = data['data']

        for deck in decks:
            deck_name = deck.pop('name')
            master_vault[deck_name] = deck


        print(page, '/', num_pages, ' ', end='')
        page = str(int(page) + 1)
        print('Page process time: ', int(time.time() - start_time))

        counter += 1

        if counter == 50 or page == num_pages:
            with open('deck_list.txt', 'w', encoding='utf-8') as file:
                file.write(str(deck_count) + '\n')
                file.write(str(master_vault))
            with open ('deck_count.txt', 'w', encoding='utf-8') as file:
                file.write(str(deck_count))

            counter = 0


        sleep(.05)    
        
    
    print(len(master_vault))




get_unique_cards(page, site)
# get_decks(page, site)


runtime = int(time.time() - program_start_time)

if runtime/60/60 > 1:
    print(f'Run Time: {runtime//3600} hours and {int(runtime%3600/60)} minutes')
elif runtime / 60 > 1:
    print(f'Run Time: {runtime//60} minutes and {int(runtime%60)} seconds')
else:
    print(f'Run Time: {runtime} seconds')



#ssl.SSLError
#keyError