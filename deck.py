
import random

class StandardDeck:

    def __init__(self):
        self.Cards = []
        self.basic_values = list(range(2, 15))  # 2-14
        # order is by suit REVERSE rank (spades highest)
        self.basic_suits = ['c', 'd', 'h', 's']

    def shuffleDeck(self):
        if len(self.Cards) > 1:
            random.shuffle(self.Cards)
        else:
            print('No need to shuffle a 1 size list...')

    def CreateDeck(self):

        # zip is cleaner code to loop over more than one list
        for suit in self.basic_suits:
            for val in self.basic_values:
                # strip the suit initial
                # each card is a sub list of [card number, suit, suit rank]
                if val == 10:
                    val = 'T'
                self.Cards.append(str(val) + suit[0])

        self.shuffleDeck()
        # error handle of allowed deck size
        if len(self.Cards) != 52:
            raise Exception("Deck Size is not 52")


