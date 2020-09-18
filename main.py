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
        for i in range (0, size):
           Mastermind.playerinput.append(int(input("Put your num ".format(i))))

if __name__ == "__main__":
    p1 = Mastermind()
    p1.Player_Input(Mastermind.playerinput,Mastermind.size)
    print(Mastermind.playerinput)
    print(Mastermind.objective)
