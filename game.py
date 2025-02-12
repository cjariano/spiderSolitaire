#from card import Card
from deck import Deck
from column import Column

class Game:
    def __init__(self):
        self.deck = Deck()
        self.columns = [Column() for i in range(10)]
        self.stock = []
    

    def deal(self):
        self.deck.shuffle()
        #deal 4 face down cards to each of 10 columns
        for _ in range(4):
            for column in self.columns:
                card = self.deck.deal_one()
                card.flip()
                column.cards.append(card)

        #deal a face down card to the first 4 columns
        for i in range(4):
            card = self.deck.deal_one()
            card.flip()
            self.columns[i].cards.append(card)
        
        #deal 1 face up card to each of 10 columns
        for column in self.columns:
            card = self.deck.deal_one()
            column.cards.append(card)

        self.stock = self.deck.cards
    
    def show_game(self):
        for column in self.columns:
            for card in column.cards:
                print(card)
            print()  # Prints a blank line to separate columns
    
    def deal_stock(self):
        for column in self.columns:
            card = self.stock.pop()
            column.cards.append(card)

    def move_card(self, from_col, to_col):
        # check if indices are within range
        if not (1 <= from_col <= len(self.columns)) or not (1 <= to_col <= len(self.columns)):
            print("Error: Column index out of range.")
            return
        
        # check if source column has cards
        if not self.columns[int(from_col-1)]:
            print("Error: Source column is empty.")
            return
        
        card = self.columns[int(from_col-1)].cards.pop()
        self.columns[int(to_col-1)].cards.append(card)

        if (not self.columns[int(from_col-1)].cards[-1].is_face_up and self.columns[int(from_col-1)].cards):
            self.columns[int(from_col-1)].cards[-1].flip()
