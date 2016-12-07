!#/usr/bin/env python3


# Counting Application
# Ask the user for name input, length of input cannot be < or == to zero

Name = input("What is your Name? ").capitalize();
while len(Name) <= 0:
    Name = input("You did not put in a name, What is your name? ").capitalize();

#Ask the user to enter an integer to count up to, if it is not a number try again

while True:
    try:

        Num = input(Name + ", please enter a number to count to: ");
        Num = int(Num);
        break
    except ValueError:
        print("Not a Number, Try again");

#Ask the user to countby which integer if value is not a int, try again
while True:
    try:
        countBy = input(Name + ", which number would you like to count by? ");
        countBy = int(countBy);
        break
    except ValueError:
        print("Not a Number, Try again");
 
   
# Identifying the variable count
count = 0;
int(count);

# If number is even start at zero, if it is not even start count at 1
if Num%2 :
    print(count +1);
else:
    print(count);
    
# While loop to count up to desired Number
while count < Num - countBy:

    count = count + countBy;

    print (count);

if Num >= countBy :
    print(Num);
else:
    print("We cannot count further");


