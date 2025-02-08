# test_game.py

from card import Card
from deck import Deck
from tableau import Tableau
from game import Game

def main():
    # Initialize the game
    game = Game()

    # Deal the cards
    game.deal()

    # Display the current state of the game
    game.show_game()

if __name__ == "__main__":
    main()
