class Card:

    # constructor
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # string representation
    def __repr__(self):
        return f"{self.rank} of {self.suit}"