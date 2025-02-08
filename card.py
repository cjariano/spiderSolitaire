class Card:

    # constructor
    def __init__(self, suit, rank, is_face_up = True):
        self.suit = suit
        self.rank = rank
        self.is_face_up = is_face_up

    def __str__(self):
        return f"{self.rank} of {self.suit}" if self.is_face_up else "X"

    def __repr__(self):
        return f"Card(suit='{self.suit}', rank='{self.rank}', is_face_up={self.is_face_up})"
    
    def flip(self):
        self.is_face_up = not self.is_face_up
    