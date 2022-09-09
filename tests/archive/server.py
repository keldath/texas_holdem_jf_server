
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cards.deck import StandardDeck
from tests.archive.deal import deal_cards
from cards.best_hand_handler import best_hand_check
from typing import List


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

        # @self.get('/create_deck')
        # async def deck():
        def create_deck():
            self.reset()  # reset the saved values -> new game
            self.state.deck_instance = StandardDeck()
            self.state.deck_instance.create_deck()
            self.state.deck_cards = self.state.deck_instance.Cards
            self.state.data.update(
                {"cards_left": len(self.state.deck_cards),
                 'deck': self.state.deck_cards,
                 'updated_deck': self.state.deck_cards
                 }
            )
            return self.state.data

        def deal_cards_all(_deck: List[str], cards: List[int]) -> dict:
            if len(_deck) == 0 or not _deck:
                return {'error': 'deck does not exists'}
            print(_deck, cards)
            result = deal_cards(_deck, cards)
            self.state.updated_deck = result['updated_deck']
            self.state.dealt_cards = result['dealt_cards']
            if cards == 2:
                self.state.player_hand = self.state.dealt_cards
            elif cards == 5:
                self.state.comm_dealt_cards = self.state.dealt_cards
            else:
                return {'error': 'card count if wrong'}

            self.state.data.update(
                {"deck": _deck,
                 "cards_left": len(self.state.updated_deck),
                 "updated_deck": self.state.updated_deck,
                 "comm_cards": self.state.comm_dealt_cards,
                 "player_hand": self.state.player_hand}
            )

            return self.state.data

        @self.get('/deal_community')
        async def community():
            create_deck()  # new game every deal of the community cards
            return deal_cards_all(self.state.data['updated_deck'], 5)

        @self.get('/deal_player')
        async def player(pa):
            return deal_cards_all(self.state.data['updated_deck'], 2)

        @self.get('/best_hand')
        async def best():
            self.state.data.update(
                {'winning_hand': best_hand_check(self.state.player_hand,
                        self.state.comm_dealt_cards)
                 }
            )
            return self.state.data

    def reset(self):
        self.state.deck_instance = ''
        self.state.deck_cards = ''
        self.state.updated_deck = ''
        self.state.comm_dealt_cards = ''
        self.state.player_hand = ''

        self.state.data = {
            "cards_left": '',
            'deck': [],
            'updated_deck': [],
            'comm_cards': [],
            'player_hand': [],
            'winning_hand': [[], '']  # expected format
        }
