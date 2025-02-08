from card import Card

class Tableau:

    def __init__(self):
        self.cards = []

    def __repr__(self):
        return f"Tableau of {len(self.cards)} cards"