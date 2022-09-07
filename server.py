
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from deck import StandardDeck
from deal import PlayersHands, CommunityCards
from handevaluator import best_hand_check

class App(FastAPI):

    def __init__(self):
        super().__init__()

        self.origins = {
            "http://localhost:3000"
        }
        self.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        self.reset()

        @self.get('/create_deck')
        async def deck():
            self.reset() # reset the saved values -> new game
            self.state.deck_instance = StandardDeck()
            self.state.deck_instance.CreateDeck()
            self.state.deck_cards = self.state.deck_instance.Cards
            self.state.data.update(
                {"cards_left": len(self.state.deck_cards),
                 'deck': self.state.deck_cards}
            )
            return self.state.data

        @self.get('/deal_community')
        async def community():
            if len(self.state.deck_cards) == 0 or not self.state.deck_cards:
                return {'error': 'deck does not exists'}
            self.state.comm_cards = CommunityCards(self.state.deck_cards)
            self.state.comm_cards.DealComm()
            self.state.updated_deck = self.state.comm_cards.updated_deck
            self.state.comm_dealt_cards = self.state.comm_cards.dealt_cards
            self.state.data.update(
                {"deck": self.state.deck_cards,
                 "cards_left": len(self.state.updated_deck),
                 'updated_deck': self.state.updated_deck,
                 'comm_cards': self.state.comm_dealt_cards}
            )
            return self.state.data

        @self.get('/deal_player')
        async def player():
            self.state.all_hands = PlayersHands(self.state.comm_cards.updated_deck)
            self.state.all_hands.DealCards()
            self.state.all_hands.updated_deck = self.state.all_hands.updated_deck
            self.state.all_hands_players_hands = self.state.all_hands.players_hands
            self.state.data.update(
                {"deck": self.state.deck_cards,
                 "cards_left": len(self.state.all_hands.updated_deck),
                 "updated_deck": self.state.all_hands.updated_deck,
                 "comm_cards": self.state.comm_dealt_cards,
                 # note - 0 means player 1, this is a future option for more players
                 "player_hand": self.state.all_hands_players_hands}
            )
            return self.state.data

        @self.get('/best_hand')
        async def best():
            self.state.data.update(
                {'Winning_hand':
                     best_hand_check(self.state.all_hands.player_hand,
                                     self.state.comm_dealt_cards)
                 }
            )
            return self.state.data

    def reset(self):
        self.state.deck_instance = ''
        self.state.deck_cards = ''
        self.state.comm_cards = ''
        self.state.updated_deck = ''
        self.state.comm_dealt_cards = ''
        self.state.all_hands = ''
        self.state.all_hands_players_hands = ''

        self.state.data = {
            "cards_left": '',
            'deck': '',
            'updated_deck': '',
            'comm_cards': '',
            'player_hand': '',
            'Winning_hand': ''
        }
