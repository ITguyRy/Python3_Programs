# Password Generator
import random



def askUser():
    strength = input("How strong would you like your password to be? ").capitalize()
    
    length = int(input("How long would you like your password to be? "))

    return strength, length
    

def pass_gen(strength, length):

    password = []
    count = 0
    if strength == "Strong":
        while length > count:
            count+=1
            PASS = chr(random.randint(33,126))
            password.append(PASS)
        print("Generated password level: {}".format(strength))
        print(''.join(password))
        
    elif strength == "Medium":
        while length > count:
            count += 1 
            order = random.randint(1,3)
            lowercase = chr(random.randint(97,122))
            uppercase = chr(random.randint(65,90))

            if order > 1:
                password.append(lowercase)
            else:
                password.append(uppercase)
        print("Generated password level: {}".format(strength))
        print(''.join(password))

    elif strength == "Weak":

        while length > count:
            count += 1 
            uppercase = chr(random.randint(65,90))
            password.append(uppercase)
            
        print("Generated password level: {}".format(strength))
        print(''.join(password))
    else:
        print('')
        print("Strength Levels are strong, medium, or weak ")
        print('')
        main()


def loop(strength, length):
    while True:
        try:
            pass_gen(strength, length)
            break
        except ValueError:
            print("Try again")
   


def main():
    strength, length = askUser()
    loop(strength, length)

main()

    

    
    
