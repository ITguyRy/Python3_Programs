# write a program that returns a list that contains only the elements that are
# common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Randomly generate two lists to test this



import random

first_list = random.sample(range(100),10)

second_list = random.sample(range(100),10)

for elem in first_list,second_list:
    if elem in first_list == elem in second_list:
    #while elem in first_list != elem in second_list:
        #if elem in first_list == elem in second_list:
            print(elem);
