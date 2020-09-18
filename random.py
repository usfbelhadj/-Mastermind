#!/usr/bin/python3
"""
"""
import random


def randomize():
    """ """
    objective = []
    for i in range(4):
        objective.append(random.randint(1, 6))
    print (objective)

if __name__ == "__main__":
   randomize()
