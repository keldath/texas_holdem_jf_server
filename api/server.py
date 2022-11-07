
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cards.cards_handler import deal_cards
from cards.best_hand_handler import best_hand_check
import json


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
        self.player = 2
        self.community = 5
        self.state.updated_deck = []

        def card_dealing(data, count):
            data = json.loads(data)
            cards_to_deal = data['cards_to_deal']
            cards_dealt = data['cards_dealt']
            if cards_to_deal != count:
                raise Exception("Error -> invalid deal cards request")
            return deal_cards(cards_dealt, cards_to_deal)

        @self.get('/deal_community')
        async def community(data):
            return card_dealing(data, self.community)

        @self.get('/deal_player')
        async def player(data):
            return card_dealing(data, self.player)

        @self.get('/best_hand')
        async def best(data):
            data = json.loads(data)
            hand = data['hand']
            _community = data['community']
            if len(hand) != self.player or len(_community) != self.community:
                raise Exception("Error -> invalid deal cards request")
            return best_hand_check(hand, _community)

