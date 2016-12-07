#Palindrome loop

#test if the word is read the same way if it were spelled backwards i.e poop


while True:
        try:
                text = input("type something that reads the same forwards and backwards: ")
                text = str(text)
                reverse = text[::-1] #slice

                if text == reverse :
                        print ("That input is a palindrome! ")

                else:
                        print ("That input is NOT a palindrome! ")
        except ValueError:
                print("Try again please ")

        
