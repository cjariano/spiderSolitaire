# test_game.py

from card import Card
from deck import Deck
from column import Column
from game import Game

def main():
    # Initialize the game
    game = Game()

    # Deal the cards
    game.deal()

    done = False
    
    while (not done):
        game.show_game()
        user_input = input("Type s to deal from stock, m to move a card: ")
        if (user_input == "s" or user_input == "S"):
            game.deal_stock()
        elif (user_input == "m" or user_input == "M"):
            from_column = int(input("What number column would you like to move the card from (1-10): "))
            to_column = int(input("What number column would you like to move the card to? (1-10): "))
            while (#mfrom_column.isnumeric() == False or to_column.isnumeric() == False or
                from_column < 1 or from_column > 10 or to_column < 1 or to_column > 10):
                print("Please enter a valid integer 1-10")
                from_column = int(input("What number column would you like to move the card from (1-10): "))
                to_column = int(input("What number column would you like to move the card to? (1-10): "))
            game.move_card(from_column, to_column)
        else:
            user_input = input("Invalid input. Type s to deal from stock, m to move a card: ")

if __name__ == "__main__":
    main()