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
        self.objective = [1 , 2 , 3 , 4]
        self.playerinput = []
        self.result = []
        self.size = 4
    def Player_Input(self):
        for i in range (1, self.size+1):
            put = (int(input("Put your num [{}] ".format(i))))
            while(len(str(put)) > 1):
                print('The size of the number must be 1')
                put = (int(input("Put your num [{}] ".format(i))))
            self.playerinput.append(put)
           
    def print_list(self):
        print(self.playerinput)
        print(self.objective)
        print(self.result)

    def compare(self):
        self.result = []
        comparelist = self.objective.copy()
        for i in range(len(self.playerinput)):
            if self.playerinput[i] == comparelist[i]:
                self.result.append(2)
                comparelist[i] = 0
            elif self.playerinput[i] in comparelist:
                self.result.append(1)
                comparelist[i] = 0
            else:
                self.result.append(0)
        self.playerinput = []
        print(self.result)
