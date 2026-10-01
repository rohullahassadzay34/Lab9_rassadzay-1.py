""" 
Match Coins Game
Rohullah Assadzay
This class represents a single, tossable coin. It only knows about its own state (heads or tails).
9/30/2026
"""
import random

class Coin:
    def __init__(self, sideup = "Tails"):
        self.__sideup = sideup

    def toss(self):
        random_number = random.randint(0, 1)
        if random_number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
    


