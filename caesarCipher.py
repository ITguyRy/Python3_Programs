#Only lowercase Alpha CAESAR CYPHER 

MAX_KEY_SIZE = 26

name = input(" What is your name? ").capitalize()

ed = input(name + ", Would you like to Encrypt or Decrypt?").capitalize()
if ed == "Encrypt":

    plaintext = input('plaintext: ')                                         
    while True:
        try:   
           key = int(input("Insert a Numeric Value 3-{}: ".format(MAX_KEY_SIZE)))
           if key >= 3 and key <= 26:
                break
           else:
               print("Your number {} is not within the range! ".format(key))
            
        except ValueError:
            print("try again")
    encryption = ''
    
    for letters in plaintext:
        if letters.isalpha():
            num = ord(letters)
            num = num + key
            
            if letters.islower():
                if num > ord('z'):
                    num = num - 26
                elif num < ord('a'):
                    num = num + 26
                encryption = encryption + chr(num)
            else:
                encryption += letters
    print ("Encrypted Message: ")
    print (encryption)

elif ed == "Decrypt":  
    cyphertext = input('Cyphertext: ')
    
    while True:
        try:   
           key = int(input("Insert a Numeric Value 1-{}: ".format(MAX_KEY_SIZE)))
           if key >= 3 and key <= 26 :
               break
           else:
               print("Your Number is not within the range! ")
        
            
        except ValueError:
            print("try again")
            
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
                decryption += letters
    print("Decrypted Message: ")
    print (decryption)

        





