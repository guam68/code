import ast
import math
import deck_processor


class Vault:
    def __init__(self):
        with open('fixed_decks.txt', 'r', encoding='utf-8') as file:
            file.readline()
            self.decks = ast.literal_eval(file.read())

        with open('fixed_unique.txt', 'r', encoding='utf-8') as file:
            file.readline()
            self.uniques = ast.literal_eval(file.read())


# returns the percentage of decks with the searched card
    def get_card_percent(self):
        search = input('Card: ')

        deck_count = 0
        for deck in self.decks:
            card_id = [k for k, v in self.uniques.items() if v['card_title'] == search][0]
            if card_id in self.decks[deck]['_links']['cards']:
                deck_count += 1

        return round(100 * deck_count / len(self.decks), 2)


    def get_avg_type(self):
        deck = deck_processor.Deck() 
        # avg_dict = {'Action':0, 'Artifact':0, 'Creature':0, 'Upgrade':0}

        # for deck in self.decks:
        #     for card in self.decks[deck]['_links']['cards']:
        #         if self.uniques[card]['card_type'] == 'Action':
        #             avg_dict['Action'] += 1
        #         elif self.uniques[card]['card_type'] == 'Artifact':
        #             avg_dict['Artifact'] += 1
        #         elif self.uniques[card]['card_type'] == 'Creature':
        #             avg_dict['Creature'] += 1
        #         elif self.uniques[card]['card_type'] == 'Upgrade':
        #             avg_dict['Upgrade'] += 1
        avg_dict = deck.get_type_count()

        for card_type in avg_dict:
            avg_dict[card_type] /= len(self.decks)

        return(avg_dict)
    


        


vault = Vault()

# print(vault.get_card_percent())
vault.get_avg_type()
# Grabber Jammer
