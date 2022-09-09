
import random


def random_card(deck):
    """
        adds a random card from the card deck
        removes the chosen value from the original list
        :returns [the chosen card, the reduced new deck]
    """
    rnd_card = random.choice(deck)
    # Uber important! make sure to update the deck after each card deal
    deck.remove(rnd_card)
    return [rnd_card, deck]


def deal_cards(deck, cnt):
    """
    deal the community cards
    :param cnt: amount of card to deal
    :param deck: exiting deck
    :return: 5 random card hand from the given deck
    """
    dealt_cards = []
    for c in range(0, cnt):
        dealt_card = random_card(deck)
        dealt_cards.append(dealt_card[0])
        updated_deck = dealt_card[1]

    return {'updated_deck': updated_deck,
            'dealt_cards': dealt_cards}



