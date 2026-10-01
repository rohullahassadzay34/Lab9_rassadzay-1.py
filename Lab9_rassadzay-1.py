"""
Rohullah Assadzay

This file runs the game. It creates the Player objects and manages the game loop and rules.

9/30/2026
"""
from player import Player

def main():
    player1 = Player("Player1")
    player2 = Player("Player2")

    print("--- Coin Match Game ---")
    print(f"Player 1 has {player1.get_wallet()}.")
    print(f"Player 2 has {player2.get_wallet()}")

    answer = input("Do you want to play? y or Y \n")
    while answer.lower() == "y":
        print("Tossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()
        print(f"Player 1 tossed {side1}, Player 2 tossed {side2} ")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"It's a Match! Player 1 wins a coin.")
            print(f"Player 1 has {player1.get_wallet()}.")
            print(f"Player 2 has {player2.get_wallet()}")

        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"No Match! Player 2 wins a coin.")
            print(f"Player 1 has {player1.get_wallet()}.")
            print(f"Player 2 has {player2.get_wallet()}")

        answer = input("Do you want to play again? y or Y \n")

main()
        






