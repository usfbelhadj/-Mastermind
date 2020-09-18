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
        for i in range (1, size+1):
            put = (int(input("Put your num [{}] ".format(i))))
            while(len(str(put)) > 1):
                print('The size of the number must be 1')
                put = (int(input("Put your num [{}] ".format(i))))
            Mastermind.playerinput.append(put)
           
    def print_list(self):
        print(Mastermind.playerinput)
        print(Mastermind.objective)
        print(Mastermind.result)

    def compare(self):
        comparelist = Mastermind.objective.copy()
        for i in range(len(Mastermind.playerinput)):
            if Mastermind.playerinput[i] == comparelist[i]:
                Mastermind.result.append(2)
                comparelist[i] = 0
            elif Mastermind.playerinput[i] in comparelist:
                Mastermind.result.append(1)
                comparelist[i] = 0
            else:
                Mastermind.result.append(0)

if __name__ == "__main__":
    
    p1 = Mastermind()
    print(p1.objective)
    p1.Player_Input()
    p1.compare()
    print(p1.objective)