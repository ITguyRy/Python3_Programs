#list over lap comprehension

import random

def randlist():

    list_one = random.sample(range(1000),100)

    list_two = random.sample(range(500),100)

    return list_one, list_two



    
def commonality(list_one, list_two):
    common_list = []
    for elements in list_one:
        if elements in list_two:
            common_list.append(elements)
    return common_list


def main():
    list_one, list_two = randlist()

    common_list = commonality(list_one, list_two)

    print(common_list)


main()
    
            
