# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

even = "You provided an Even Number! ";

odd = "You provided an Odd Number! ";

four = "You provided a number divisable by 4! ";


num = int(input("Provide a number: "));

 # If the number is a multiple of 4, print out a different message.
if num % 4 == 0 :
    print(four);
else:
    
    div = int(num % 2);
    if div == 0:
        print (even);
    
    else:
        print(odd);



#2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).

#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print ("Lets try another one. ");

num_two = int(input("Provide a number: "));

divBy = int(input("How would you like to divide that number? "));


result = int(num_two / divBy)

evenly = "That divides evenly! ";
odd =" That did not divide evenly...result was " + str(result);

if num_two % divBy == 0 :
    print (evenly);
else :
    print (odd);

