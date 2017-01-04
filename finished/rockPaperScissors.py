# Rock Paper Scissors Game by Ryan Ung

import random
#popular variables
userWins = "You won!"
userLose = "You lost!"
cpWin = "Opponent won!"
rock = ''
paper =''
scissor = ''
space = ''

#Random generated range translated to RPS
CP = random.randrange(1,99)
if CP <= 33:
    CP = 'scissors'
elif CP >= 33 and CP <= 66:
    CP = 'paper'
else:
    CP = 'rock'

#User input RPS


user = input("Choose rock, paper, or scissors: ").lower()
print(space)


# RPS winning code
if user == 'scissors' and CP == 'paper':
    print(userWins)
elif user =='paper' and CP == 'rock':
    print(userWins)
elif user == 'rock' and CP == 'scissors':
    print(userWins)
elif user == CP:
    print('Draw! ')
else:
    print(cpWin)



print("Opponent chose: " + str(CP))
print (space)

again = input("Would you like to play again? ").lower()


# Play again if user types (y)es
while again == 'yes' or again == 'y' :
    CP = random.randrange(1,99)
    if CP <= 33:
        CP = 'scissors'
    elif CP >= 33 and CP <= 66:
        CP = 'paper'
    else:
        CP = 'rock'


    user = input("Choose rock, paper, or scissors: ").lower()
    print(space)

    if user == 'scissors' and CP == 'paper':
        print(userWins)
    elif user =='paper' and CP == 'rock':
        print(userWins)
    elif user == 'rock' and CP == 'scissors':
        print(userWins)
        
    elif user == CP:
        print('Draw! ')
    else:
        print(cpWin)
        
    print("Opponent chose: " + str(CP))
    print('')
    
    again = input("Would you like to play again? ").lower()

    




