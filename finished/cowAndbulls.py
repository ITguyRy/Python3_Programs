import random



def user_guess():
    while True:
        try:    
            guess = int(input("Guess the four digit number: " ))
            if guess < 9999 and guess > 999:
                guess = list(str(guess))
                return guess
                break
            else:
                print("Guess 4 digits please ")
        except ValueError:
            print("Try again ")
            

def rand_four_digits():
    digits = []
    while len(digits) < 4:
        four = random.randint(0,9)
        digits.append(four)
    print(digits)
    return digits


def answer_check(guess,digits):
    
    guess = list(map(int,guess))
    print(guess)
       
    correct = []
    for elements in guess:
        if elements in digits:
            elements = str(elements)
            correct.append(elements)
        cows = len(correct)
        bulls = 4 - cows
        
    print("{} cows,".format(cows) + " {} bulls".format(bulls))
    


            
def loop_check(guess,digits):
    guess = list(map(int,guess))
    count = 1
    while guess != digits:
        count+=1
        guess = user_guess()
        answer_check(guess,digits)
        guess = list(map(int,guess))
        print(guess)
        print(digits)
    print("Number of times guessed: {}".format(count))


def main():
    digits = rand_four_digits()
    guess = user_guess()
    answer_check(guess,digits)
    loop_check(guess,digits)
    

main()
    
