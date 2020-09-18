#!/home/achref/Desktop/Holberton/Mastermind/Mastermind/bin/python3
"""
"""
class Mastermind():
    objective = []
    playerinput = []
    result = []
    size = 4
    def __init__(self):
        pass
    def Player_Input(self,playerinput, size):
        for(i in range [0 , size]):
            playerinput.append(int(input("Put your num => {}".format(i))))

