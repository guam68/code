# 370 base cards, 329 found mavericks (04 JAN)
import ast
import time


program_start_time = time.time()

print('Getting card data...')
with open('card_list.txt', 'r', encoding='utf-8') as file:
    card_count = file.readline()
    uniques = ast.literal_eval(file.read())
print('Card data added!\n')

print('Getting deck data...')
with open('deck_list.txt', 'r', encoding='utf-8') as file:
    deck_count = file.readline()
    decks = ast.literal_eval(file.read())
print('Deck data added!\n')


def get_mavericks(uniques):
    
    with open('fixed_unique.txt', 'r', encoding='utf-8') as file:
        card_count_unique = file.readline()
        uniques = ast.literal_eval(file.read())
    
    
    mavericks = {}
    for card in uniques:
        if uniques[card]['is_maverick']:
            if uniques[card]['card_title'] in mavericks:
                mavericks[uniques[card]['card_title']].append(uniques[card]['house'])
            else:
                mavericks[uniques[card]['card_title']] = [uniques[card]['house']]
    return mavericks, len(mavericks)


def fix_card_list(uniques):
    card_dict = {}
    for card in uniques:
        card_id = card.pop('id')
        card_dict[card_id] = card

    with open('fixed_unique.txt', 'w', encoding='utf-8') as file:
            file.write(str(card_count))
            file.write(str(card_dict))
    print(len(card_dict))


# def fix_deck_list(decks):
#     deck_dict = {}
#     for deck in decks:
#         deck_name= deck.pop('name')
#         deck_dict[deck_name] = deck

#     with open('fixed_decks.txt', 'w', encoding='utf-8') as file:
#             file.write(str(deck_count))
#             file.write(str(deck_dict))


def get_deck_info():
    pass


def get_card_type():

    action_list = []
    creature_list = []
    artifact_list = []
    upgrade_list = []

    name = input('Deck Name: ')
    card_list = decks[name]['_links']['cards']

    for card in card_list:
        if uniques[card]['card_type'] == 'Action':
            action_list.append(card)
        elif uniques[card]['card_type'] == 'Artifact':
            artifact_list.append(card)
        elif uniques[card]['card_type'] == 'Creature':
            creature_list.append(card)
        elif uniques[card]['card_type'] == 'Upgrade':
            upgrade_list.append(card)
    
    return (action_list, creature_list, artifact_list, upgrade_list)

    print(action_list)


def get_num_unique():
    with open('fixed_unique.txt', 'r', encoding='utf-8') as file:
        file.readline()
        uniques = ast.literal_eval(file.read())

    card_counter = {}

    for deck in decks:
        deck_card_dict = decks[deck]['_links']['cards']
        for card in deck_card_dict:
            if uniques[card]['card_title'] in card_counter:
                card_counter[uniques[card]['card_title']] += 1
            else:
                card_counter[uniques[card]['card_title']] = 1

    cc_list = list(card_counter.items())
    cc_list.sort(key=lambda tup: tup[1], reverse=True)

    print(cc_list)




fix_card_list(uniques)
# get_num_unique()
# print(get_card_type())
# mavs = get_mavericks(uniques)
# print(mavs)
# print(len(decks))


runtime = int(time.time() - program_start_time)

if runtime/60/60 > 1:
    print(f'Run Time: {runtime//3600} hours and {int(runtime%3600/60)} minutes')
elif runtime / 60 > 1:
    print(f'Run Time: {runtime//60} minutes and {int(runtime%60)} seconds')
else:
    print(f'Run Time: {runtime} seconds')