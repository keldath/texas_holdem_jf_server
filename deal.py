
import random


def DealCard(deck):
    """
        adds a random card from the card deck
        removes the chosen value from the original list
        :returns [the chosen card, the reduced new deck]
    """
    rnd_card = random.choice(deck)
    # Uber important! make sure to update the deck after each card deal
    deck.remove(rnd_card)
    return [rnd_card, deck]


class PlayersHands:

    def __init__(self, deck):
        # if more than one player, dealing cards must be in ->
        # order - in case of more than player...
        self.cards_per_player = 2
        self.player_hand = []
        self.cards_dealt = 0
        self.updated_deck = deck
        self.DealCard = DealCard  # global re usable fn

    def DealCards(self):

        while True:

            post_card_deal = self.DealCard(self.updated_deck)
            self.player_hand.append(post_card_deal[0])
            self.updated_deck = post_card_deal[1]  # new reduced deck
            self.cards_dealt += 1

            # stop dealing after the correct num of cards have been dealt
            if self.cards_per_player == self.cards_dealt:
                break


class CommunityCards:

    def __init__(self, deck):
        self.cards_allowed = 5
        self.dealt_cards = []
        self.updated_deck = deck
        self.DealCard = DealCard  # global re usable fn

    def DealComm(self):
        for c in range(0, self.cards_allowed):
            dealt_card = self.DealCard(self.updated_deck)
            self.dealt_cards.append(dealt_card[0])
            self.updated_deck = dealt_card[1]



