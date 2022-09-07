
from deck import StandardDeck
from deal import PlayersHands, CommunityCards
from handevaluator import best_hand_check
import uvicorn
from server import App


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
    # print(all_hands.players_hands)

    # in case we have more than one player (not in the requirement)
    best_hand_check(all_hands.player_hand, comm_cards.dealt_cards)


if __name__ == '__main__':
    #init_app = App()
    #uvicorn.run("server:App", host="localhost", port=8080, reload=True)
    # manual test
    manual_test()

