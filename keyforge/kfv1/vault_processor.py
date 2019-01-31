import ast
import math
import time


# print('\nReading from vault...')
# with open('formated_decks.txt', 'r', encoding='utf-8') as file:                          # Change back to deck_list!!
#     count = file.readline()
#     # decks = file.read()
#     decks = ast.literal_eval(file.read())
# print('Vault copied!\n')

# with open('formated_decks.txt', 'r', encoding='utf-8') as file:                          
#     count = file.readline()
#     text = [] 
#     for line in file:
#         text.append(line)

#     decks = ast.literal_eval(''.join(text))

with open('fixed_unique.txt', 'r', encoding='utf-8') as file:
    file.readline()
    uniques = ast.literal_eval(file.read())


class Vault:
    def __init__(self, decks, uniques):
        self.decks = decks
        self.uniques = uniques

    def format_decklist(self):
        big_string = ''
        test = decks.split(f'}}, ')         

        # for deck in test:
        #     big_string += deck + f'}},\n'

        big_string = ''.join([deck + f'}},\n' for deck in test])

        big_string = count + big_string[:-3]

        with open('formated_decks.txt', 'w', encoding='utf-8') as file:
            file.write(big_string)

        # print(len(test))


# returns the percentage of decks with the searched cards
    def get_card_percent(self):
        search = []
        card_id = []
        deck_count = 0

        while True:
            card = (input('Card: '))
            if card == 'x':
                break
            search.append(card)
        
        with open('formated_decks.txt', 'r', encoding='utf-8') as file:                          
            count = file.readline()
            for line in file:
                ast.literal_eval(line)
                for i in range(len(search)):
                    card_id.append([k for k, v in self.uniques.items() if v['card_title'] == search[i]])
                    


        for deck in self.decks:
            for i in range(len(search)):
                card_id.append([k for k, v in self.uniques.items() if v['card_title'] == search[i]])
            print(card_id)
            quit()
            if card_id in self.decks[deck]['_links']['cards']:
                deck_count += 1

        return round(100 * deck_count / len(self.decks), 2)


    def get_avg_type(self, deck1):
        avg_dict = deck1.get_type_count()

        for card_type in avg_dict:
            avg_dict[card_type] /= len(self.decks)

        return(avg_dict)
    
    def get_avg_pwr(self):
        power_list = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        num_decks = len(self.decks)

        for deck in self.decks:
            flag = False
            cards = self.decks[deck]['_links']['cards']
            for card in cards:
                if card not in self.uniques:
                    print(card)
                    flag = True
                    num_decks -= 1
                    break
            if flag == False:
                for card in cards:
                    pwr = self.uniques[card]['power']
                    if pwr > 0:
                        power_list[pwr] += 1

        print([(i,round(power/num_decks,1)) for i, power in enumerate(power_list)])        
        power_list = [(round(power/num_decks)) for power in power_list]
        print(power_list)




class Deck:
    def __init__(self, decks, uniques):
        self.decks = decks
        self.uniques = uniques
        

# returns four lists with all cards of corresponding type
    def get_card_type(self, user_input, deck):    
        action_list = []
        creature_list = []
        artifact_list = []
        upgrade_list = []

        if user_input:
            name = input('Deck Name: ')
            card_list = self.decks[name]['_links']['cards']
        else:
            card_list = self.decks[deck]['_links']['cards']

        for card in card_list:
            if self.uniques[card]['card_type'] == 'Action':
                action_list.append(card)
            elif self.uniques[card]['card_type'] == 'Artifact':
                artifact_list.append(card)
            elif self.uniques[card]['card_type'] == 'Creature':
                creature_list.append(card)
            elif self.uniques[card]['card_type'] == 'Upgrade':
                upgrade_list.append(card)

        return (action_list, artifact_list, creature_list, upgrade_list)


# returns (avg creature power) and (a list with the index as creature power and value as number of cards with that value)
    def get_strengths(self):   
        _, creatures, _, _ = self.get_card_type()

        power_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in creatures:
            power_count[int(self.uniques[card]['power'])] += 1

        sum_str = 0
        for i, val in enumerate(power_count):
            sum_str += i * val
        avg_str = round(sum_str / len(creatures), 2)
        print(avg_str)
        return power_count


# returns a dict with the house as key and list of card ids as values
    def separate_houses(self):
        name = input('Deck Name: ')
        card_list = self.decks[name]['_links']['cards']

        houses = {}
        
        for card in card_list:
            print(card)
            if self.uniques[card]['house'] in houses:
                houses[self.uniques[card]['house']].append(card)
                
            else:
                houses[self.uniques[card]['house']] = [card]
                print(houses)

        print(houses)


    def get_std_dev(self, vault):
        std_dev = vault.get_avg_type(self)      # dict
        print(std_dev)
        sum_of_squared = 0

        for i, card_type in enumerate(std_dev):
            mean = std_dev[card_type]           # float
            type_key = list(std_dev.keys())[i]  # string (key of std_dev)

            for deck in vault.decks:            # deck: string (key of vault.decks)
                card_type = self.get_card_type(False, deck)[i]     # card_type: list
                sum_of_squared += (len(card_type) - std_dev[type_key])**2
            std_dev[type_key] = math.sqrt(sum_of_squared / len(vault.decks))
        
        print(std_dev)


    def get_type_count(self):
        type_count_dict = {'Action':0, 'Artifact':0, 'Creature':0, 'Upgrade':0}

        for deck in self.decks:
            for card in self.decks[deck]['_links']['cards']:
                if self.uniques[card]['card_type'] == 'Action':
                    type_count_dict['Action'] += 1
                elif self.uniques[card]['card_type'] == 'Artifact':
                    type_count_dict['Artifact'] += 1
                elif self.uniques[card]['card_type'] == 'Creature':
                    type_count_dict['Creature'] += 1
                elif self.uniques[card]['card_type'] == 'Upgrade':
                    type_count_dict['Upgrade'] += 1
        
        return type_count_dict       


vault = Vault(decks, uniques)
deck1 = Deck(decks, uniques)

# deck.get_strengths()
# # deck.separate_houses()
# deck1.get_std_dev(vault)
# # Rhothomir “Stile” l’Iperattivo

# vault.format_decklist()

vault.get_avg_pwr()

# print(vault.get_card_percent())
# print(vault.get_avg_type(deck1))
# # Grabber Jammer
