from spiderSolitaire.card import Card

class Tableau:

    def __init__(self):
        self.cards = [Card()]

    def __repr__(self):
        return f"Tableau of {len(self.cards)} cards"