#CAESAR CYPHER Application


#Imported regular expressions
import re

# Assigning popular strings to variables
valueError = "Try it again"
typeError = "Try it again, this time in lower alphabets ONLY! "

# Maximum key size as a reminder
MAX_KEY_SIZE = 26

#Ask the user for their name
name = input(" What is your name? ").capitalize()

# Error handling so we only get the inputs (E)ncrypt or (D)ecrypt
while True:
    try:    
        ed = input(name + ", Would you like to Encrypt or Decrypt? ").capitalize()
        if ed == "Encrypt" or ed == "E" or ed == "Decrypt" or ed == "D":
            break
        else:
            print("You did not type in the right mode! ")
    except ValueError:
            print(valueError)
            
# If the user typed (E)ncrypt run Error handler loop
if ed == "Encrypt" or ed == "E":
    while True:
        try:
           plaintext = input('plaintext: ')
           if re.match("^[a-z]*$",plaintext): #if user input matches regex beginning(^) with lowercase [a-z] and ending($) allow a break.
               break
           else:    # otherwise print out the typeError
               print(typeError)
        except ValueError:
            print(valueError)
            
    while True:
        try:   
           key = int(input("Insert a Numeric Value 3-{}: ".format(MAX_KEY_SIZE))) # Placeholder
           if key >= 3 and key <= 26: # if user inputted a key >= 3 and if it is lower than 27, allow a break.
                break
           else:    
               print("Your number {} is not within the range! ".format(key))  
        except ValueError:
            print(valueError)

    
    encryption = ''

    # For each chars stored in plaintext
    for letters in plaintext:
        if letters.isalpha(): # checks if each char are in the alphabet
            num = ord(letters)  # the ordinal digits of those chars will be stored in num
            num = num + key     # To encrypt the message we add the key with the ordinal stored in num
            
            if letters.islower(): #if the chars are lowercase (which they will always be)
                if num > ord('z'):  # and if a char is greater than ord('z')(122) 
                    num = num - 26      # subtract 26 so we can wrap around to the beginnning of the alphabet
                elif num < ord('a'):# if a char is lower than ord('a')(97)
                    num = num + 26      # add 26 to wrap around towards the end of the alphabet
                encryption = encryption + chr(num) #concatenate empty variable to char so we can do it for each letter
            else:
                encryption = encryption + letters #return non encrypted text if errors occur
    print ("Encrypted Message: ")
    print (encryption)

elif ed == "Decrypt" or ed == "D":

    while True:
        try:
            cyphertext = input('Cyphertext: ')
            if re.match("^[a-z]*$",cyphertext):
                break
            else:
                print(typeError)
        except ValueError:
            print (valueError)
    
    while True:
        try:   
           key = int(input("Insert a Numeric Value 3-{}: ".format(MAX_KEY_SIZE)))
           if key >= 3 and key <= 26 :
               break
           else:
               print("Your Number is not within the range! ")
        
            
        except ValueError:
            print(valueError)
            
    decryption = ''
    
    for letters in cyphertext:
        if letters.isalpha():
            num = ord(letters)
            num = num - key
            
            if letters.islower():
                if num > ord('z'):
                    num = num - 26
                elif num < ord('a'):
                    num = num + 26
                decryption = decryption + chr(num)
            else:
                decryption = decryption + letters
    print("Decrypted Message: ")
    print (decryption)

        





