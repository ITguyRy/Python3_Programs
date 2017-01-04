import random

def rand_ol():

    ul = random.sample(range(10),10)
    ol = sorted(ul)
    return (ol)


def user_input():

    number = int(input("Provide a number to check the list: "))

    return number


def check(ol,number):

    for i in ol:
        if number == i:
            print("Your number is on the list")
            break
        else:
            print("Your number is not on the list")
            break


def main():
    ol = rand_ol()
    number = user_input()
    check(ol,number)

main()

    
