from card import Card
from deck import Deck
from tableau import Tableau

class Game:
    def __init__(self):
        self.deck = Deck()
        self.tableaus = [Tableau() for i in range(10)]
        self.stock = []
    

    def deal(self):
        self.deck.shuffle()
        #deal 4 face down cards to each of 10 tableaus
        for _ in range(4):
            for tableau in self.tableaus:
                card = self.deck.deal_one()
                card.flip()
                tableau.cards.append(card)

        #deal a face down card to the first 4 tableaus
        for i in range(4):
            card = self.deck.deal_one()
            card.flip()
            self.tableaus[i].cards.append(card)
        
        #deal 1 face up card to each of 10 tableaus
        for tableau in self.tableaus:
            card = self.deck.deal_one()
            tableau.cards.append(card)

        self.stock = self.deck.cards
    
    def show_game(self):
        for tableau in self.tableaus:
            for card in tableau.cards:
                print(card)
            print()  # Prints a blank line to separate tableaus
    
    def deal_stock(self):
        for tableau in self.tableaus:
            card = self.stock.pop()
            tableau.cards.append(card)

    def move_card(self, int1, int2):
        card = self.tableaus[int1-1].tableau.cards.pop()
        self.tableaus[int2-1].tableau.append(card)
