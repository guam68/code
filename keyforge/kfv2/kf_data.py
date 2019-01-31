import requests
import re
import json
import time
from time import sleep
import ast
import credentials as cred
from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import logging

program_start_time = time.time()

logging.basicConfig(filename='error.log', filemode = 'a', level=logging.DEBUG)
page = '1' 
site = ('https://www.keyforgegame.com/api/decks/?page=','&page_size=25&links=cards&ordering=-date') 

# Get the number of pages required to process (working for v2)
def get_num_pages():
    response = requests.get(site[0] + page + site[1]).json()
    count = int(response['count'])
    pages = count // 25
    return pages


def get_unique_cards(page, site):
    con = None
    con = connect(dbname='keyforge', user=cred.login['user'], host='localhost', password=cred.login['password'])

    pages = get_num_pages()
    page = pages

    for i in range(pages,0,-1):        # Range should be pages to 0 here. Changed to get base cards
        url = site[0] + str(page) + site[1]
        start_time = time.time()
        card_list = []
        deck_list = []
        house_list = []
        deck_card_list = []

        try:
            data = requests.get(url).json()
            cards = data['_linked']['cards']
            decks = data['data']
           
        except requests.exceptions.SSLError:
            logging.exception(f'SSLError on page: {page}')
            print('SSLError timeout. Sleeeeeep')
            sleep(5)
            print('Collection resumed')
            continue

        for card in cards:
            card = list(card.values())
            card_list.append(card) 

        for deck in decks:
            deck_id = deck['id']
            del deck['is_my_deck']
            del deck['notes']
            del deck['is_my_favorite']
            del deck['is_on_my_watchlist']
            del deck['casual_wins']
            del deck['casual_losses']
            deck = list(deck.values())
            links = deck.pop(-1)

            house_list = links['houses']
            deck_card_list = links['cards']
            try:
                add_deck(deck, con)
                add_deck_houses(deck_id, house_list, con)
                add_deck_cards(deck_id, deck_card_list, con)
            except:
                logging.exception(f'Error when inserting data on page: {page}')


        add_cards(card_list, con)

        print(pages - page, '/', pages, ' ', end='')
        page -= 1
        print('Page process time: ', int(time.time() - start_time))

        sleep(.5)
    
    
    con.close()

        
def add_cards(cards, con):
    for card in cards:
        sql = """
            insert into cards
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            on conflict do nothing;       
        """
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute(sql, (card))
        cur.close() 


def add_deck(deck, con):
    sql = """
        insert into decks
        values(%s,%s,%s,%s,%s,%s,%s)
        on conflict (id) do update
        set (power_level, chains, wins, losses)
        = (excluded.power_level, excluded.chains, excluded.wins, excluded.losses);
    """
    
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute(sql, (deck))
    cur.close() 


def add_deck_houses(deck_id, house_list, con):
    sql = """
        insert into deck_houses
        values(%s,%s,%s,%s)
        on conflict do nothing;       
    """
    add_list = [deck_id] + house_list
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute(sql, (add_list))
    cur.close() 
    

def add_deck_cards(deck_id, deck_card_list, con):
    sql = """
        insert into deck_cards
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        on conflict do nothing;       
    """
    add_list = [deck_id] + deck_card_list
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute(sql, (add_list))
    cur.close()


get_unique_cards(page, site)


runtime = int(time.time() - program_start_time)

if runtime/60/60 > 1:
    print(f'Run Time: {runtime//3600} hours and {int(runtime%3600/60)} minutes')
elif runtime / 60 > 1:
    print(f'Run Time: {runtime//60} minutes and {int(runtime%60)} seconds')
else:
    print(f'Run Time: {runtime} seconds')