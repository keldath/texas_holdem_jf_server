
import random
from typing import List


def deal_cards(dealt: List[str], amount: int) -> list:

    values = list(range(2, 10)) + (['T', 'J', 'Q', 'K', 'A'])
    suits = ['c', 'd', 'h', 's']
    deck = []
    for val in values:
        val = str(val)
        # faster then another loop...
        deck.append(val + suits[0])
        deck.append(val + suits[1])
        deck.append(val + suits[2])
        deck.append(val + suits[3])

    random.shuffle(deck)

    drew = 0
    cards = []
    while drew < amount:
        pick_a_card = random.choice(deck)
        deck.remove(pick_a_card)  # for the next iteration
        if pick_a_card not in dealt: # no need for cards drew b4
            cards.append(pick_a_card)
            drew += 1

    # this is a double check for the deck and the cards
    # cannot happen but worthwhile to verify
    for card in cards:
        if card in deck:
            raise Exception("Error -> Duplicate card found")

    return cards




