def sentence():
    user_input = str(input("Provide a sentence to reverse: ").capitalize())
    return user_input

def reverse(user_input):
    user = user_input.split()
    user2 = user[::-1]
    
    print(', '.join(user2).capitalize())

def main():
    user_input = sentence()
    reverse(user_input)
    return





main()
    
    
