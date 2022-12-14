
import random


class StandardDeck:

    def __init__(self):
        self.Cards = []
        self.basic_values = list(range(2, 10))  # 2-9
        self.top_cards = ['T', 'J', 'Q', 'K', 'A']
        # order is by suit REVERSE rank (spades highest)
        self.basic_suits = ['c', 'd', 'h', 's']

    def shuffle_deck(self):
        if len(self.Cards) > 1:
            random.shuffle(self.Cards)
        else:
            print('No need to shuffle a 1 size list...')

    def create_deck(self):

        for suit in self.basic_suits:
            for val in self.basic_values:
                self.Cards.append(str(val) + suit)
            for val in self.top_cards:
                self.Cards.append(str(val) + suit)

        self.shuffle_deck()
        # error handle of allowed deck size
        if len(self.Cards) != 52:
            raise Exception("Deck Size is not 52")