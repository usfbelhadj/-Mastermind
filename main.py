#!/usr/bin/python3
"""
"""
from choise import randomize


class Mastermind():
    objective = randomize()
    playerinput = []
    result = []
    size = 4
    def __init__(self):
        pass
    def Player_Input(self,playerinput, size):
        for i in range (0 , size):
            playerinput.append(int(input("Put your num => {}".format(i))))

if __name__ == "__main__":
   print(Mastermind.objective)
