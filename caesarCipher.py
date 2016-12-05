# decode ascii encoded CAESAR CYPHER - written for Python 3
# to run in Python 2.7, replace 'input' with 'raw_input'


name = input(" What is your name? ").capitalize()

ed = input(name + ", Would you like to Encrypt or Decrypt?").capitalize()



if ed == "Decrypt" :
    strASCII = '' # this will hold all 256 ASCII chars

    cyphertext = input('Cyphertext: ') # the encrypted string we want to decode
    key = int(input('Key: '))  # hint: less than 10

    while key < 3:
        try:   
            key = int(input('The key you provided was less than 3, go higher: '))
            
        except ValueError:
            print("try again")
        

    for i in range(97,122):
        strASCII = strASCII + chr(i)  # create string with all 256 ASCII characters
        

    for x in range(len(cyphertext)):
        m = strASCII.find(cyphertext[x])    # m = position of this char within strASCII
        print(cyphertext[x] + ' = ' + str(m) + ' = ' + chr(m-key))



else:
    
    strASCII = '' 

    plaintext = input('Plaintext: ') 
    key = int(input('Key: ')) 

    while key < 3:
        try:   
            key = int(input('The key you provided was less than 3, go higher: '))
        except ValueError:
            print("try again")

    for i in range(256):
        strASCII = strASCII + chr(i)  

    for x in range(len(plaintext)):
        m = strASCII.find(plaintext[x])    
        print(plaintext[x] + ' = ' + str(m) + ' = ' + chr(m+key))

    


