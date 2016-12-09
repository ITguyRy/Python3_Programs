
def dupeList():
    
    a = []
    MAX_LIST = int(input("How long do you want your list to be? "))
    count = 0
    
    while MAX_LIST > count:
        num = MAX_LIST - count
        count+= 1
        num_input = int(input("Provide {} numbers for the list(add dupes): ".format(num)))
        a.append(num_input)
    return a
    




def newList(a):

    b = set(a)
    b = list(b)

    print(b)


def main():
    a = dupeList()
    newList(a)


main()
