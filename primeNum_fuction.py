


def num_input():

    num = int(input("Give me the number, I will tell you if it is prime: "))
    return num



def prime(num):

    if num%2 == 0:
        print("Your number '{}' is a prime number! ".format(num))
    else:
        print("Your number '{}' is not a prime number! ".format(num))


def main() :
    num = num_input()
    prime(num)

main()
