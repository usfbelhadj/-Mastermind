#!/usr/bin/python3
"""
"""
from choise import randomize


class Mastermind():
    objective = [1 , 2 , 3 , 4]
    playerinput = []
    result = []
    size = 4
    def __init__(self):
        pass
    def Player_Input(self,playerinput, size):
        for i in range (0, size):
           Mastermind.playerinput.append(int(input("Put your num ".format(i))))
           
    def print_list(self):
        print(Mastermind.playerinput)
        print(Mastermind.objective)
        print(Mastermind.result)

    def compare(self, playerinput, objective, result):
        for i in range(len(Mastermind.playerinput)):
            if Mastermind.playerinput[i] == Mastermind.objective[i]:
                Mastermind.result.append(2)
            elif Mastermind.playerinput[i] in Mastermind.objective:
                Mastermind.result.append(1)
            else:
                Mastermind.result.append(0)


if __name__ == "__main__":
    p1 = Mastermind()
    p1.Player_Input(Mastermind.playerinput,Mastermind.size)
    p1.print_list()
    p1.compare(Mastermind.playerinput, Mastermind.objective, Mastermind.result)
    p1.print_list()