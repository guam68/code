import ast
import math
import vault_processor

class Deck:
    def __init__(self):
        with open('fixed_decks.txt', 'r', encoding='utf-8') as file:
            file.readline()
            self.decks = ast.literal_eval(file.read())

        with open('fixed_unique.txt', 'r', encoding='utf-8') as file:
            file.readline()
            self.uniques = ast.literal_eval(file.read())
        

# returns four lists with all cards of corresponding type
    def get_card_type(self):    
        action_list = []
        creature_list = []
        artifact_list = []
        upgrade_list = []

        name = input('Deck Name: ')
        card_list = self.decks[name]['_links']['cards']

        for card in card_list:
            if self.uniques[card]['card_type'] == 'Action':
                action_list.append(card)
            elif self.uniques[card]['card_type'] == 'Artifact':
                artifact_list.append(card)
            elif self.uniques[card]['card_type'] == 'Creature':
                creature_list.append(card)
            elif self.uniques[card]['card_type'] == 'Upgrade':
                upgrade_list.append(card)

        print(len(action_list), len(artifact_list), len(creature_list), len(upgrade_list))
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
        std_dev = vault.get_avg_type()
        card_types = self.get_card_type()
        print(std_dev)

        for i, card_type in enumerate(std_dev):
            mean = std_dev[card_type]
            std_dev[card_type] = math.sqrt((len(card_types[i]) - std_dev[card_type])**2)

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




deck = Deck()

# deck.get_strengths()
# deck.separate_houses()
deck.get_std_dev(vault)
# Rhothomir “Stile” l’Iperattivo
