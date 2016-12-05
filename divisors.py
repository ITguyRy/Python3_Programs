# Create a program that asks the user for a number and then prints out a list of all the divisors
# of that number. example, 13 is a divisor of 26 because 26 / 13 has no remainder.)




divList = []

#for elem in x :
 #   print (elem);

num = int(input("Provide a number to check divisables:" ));

x = range(1,num+1);

for elem in x:
    if num % elem == 0:
        divList.append(elem);
        
print(divList);
