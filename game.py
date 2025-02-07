from spiderSolitaire.card import Card
from spiderSolitaire.deck import Deck
from spiderSolitaire.tableau import Tableau

class Game:
    def __init__(self):
        self.deck = Deck()
        self.tableaus = [Tableau() for i in range(10)]
        self.stock = [Card()]
    
    def deal(self):
        for i in range(4):
            for t in self.tableaus:
                t.cards.append(self.deck.deal_one())
                t.cards[i].faceup(False) # make facedown

        for i in range(4):
            self.tableaus[i].cards.append(self.deck.deal_one())
            self.tableaus[i].cards[i].faceup(False) # make facedown

        for t in self.tableaus:
            t.cards.append(self.deck.deal_one()) 
            t.cards[-1].faceup(True) # make faceup

        self.stock = self.deck