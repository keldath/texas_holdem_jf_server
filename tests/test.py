
from pathlib import Path
import sys
from cards.cards_handler import StandardDeck
from tests.archive.deal import PlayersHands, CommunityCards
from cards.best_hand_handler import best_hand_check

# add py path tp system path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

def manual_test():

    # create the deck
    deck_instance = StandardDeck()
    deck_instance.CreateDeck()
    # print(deck_instance.Cards)  # org deck

    # draw the community cards
    comm_cards = CommunityCards(deck_instance.Cards)
    comm_cards.DealComm()
    # print(comm_cards.updated_deck)
    # print(comm_cards.dealt_cards)

    # deal hands
    all_hands = PlayersHands(comm_cards.updated_deck)
    all_hands.DealCards()
    # print(all_hands.updated_deck)  # deck post player deal
    # print(all_hands.player_hand)

    # in case we have more than one player (not in the requirement)
    best_hand_check(all_hands.player_hand, comm_cards.dealt_cards)


if __name__ == '__main__':
    manual_test()

