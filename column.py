# from card import Card

class Column:

    def __init__(self):
        self.cards = []

    def __repr__(self):
        return f"Column of {len(self.cards)} cards"