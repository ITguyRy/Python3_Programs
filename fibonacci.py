#Fibonnaci python program - Ryan Ung estimated 2 hours to complete 

def user_input():

    fib_input = int(input("How many fibonacci numbers would you like? "))

    fib_seq = int(input("What fibonacci sequence would you like to go by? "))

    return fib_input, fib_seq



def fib_formula(fib_input,fib_seq):
    count = 0
    int(count)
    
    fibonacci = []
    fibonacci.append(0)
    
    while fib_input > count:
        count+=1
    
        fibonacci.append(fib_seq)

        fib_seq = fibonacci[count -1] + fib_seq

    print (fibonacci)


def main():
    fib_input, fib_seq = user_input()
    fib_formula(fib_input,fib_seq)
    

main()

    
    

    






    
