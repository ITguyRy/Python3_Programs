#pull the first and last numbers from random list and put it into a new list

import random


def randlist():

    one = random.sample(range(100),10)
    return one


def listEnds(one):
    
    firstlast = []
    first = one[1]
    last = one[-1]
    
    firstlast.append(first)
    firstlast.append(last)
        
    print(firstlast)


def main():
    one = randlist()
    last = listEnds(one)


main()
