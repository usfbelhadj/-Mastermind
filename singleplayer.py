#!/usr/bin/python3
"""
The single player virsion of the game
""""
import random
from mastermind import Mastermind

class SinglePlayer(Mastermind):
    """
    Full the list objictive with random numbers
    """
    def __init__(self):
        """
        inisialise objictive
        """
        self.objective = SinglePlayer.randomize()
    def randomize():
        """
        full the objictive with random numbers
        """
        objective = []
        for i in range(4):
            objective.append(random.randint(1, 6))
        return (objective)

if __name__ == "__main__":
    i = 0
    p1 = SinglePlayer()
    print(p1.objective)
    while p1.result != [ 2,2,2,2] and i < 9:
        p1.Player_Input()
        print(p1.playerinput)
        p1.compare()
        print(p1.result)
        i += 1