from card import Card
import random


class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks for _ in range(2)]

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop() if self.cards else None