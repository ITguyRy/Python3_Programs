import random
import sys

def randomNum () :
    Num = random.randint(1,9)
    return Num


def userGuess() :
   
    user = int(input("Guess the right number: "))
    return user
            


def check(Num,user) :
    
    if Num > user:
        print("You guessed too low!")
    elif Num < user:
        print("You guessed too high!")
    else:
        print("You guessed the right number!")
    print("Type exit to leave ")




def main():
    while True:
        try:
            Num = randomNum()
            user = userGuess()
            check(Num,user)
        

        except ValueError:
            break


main()


