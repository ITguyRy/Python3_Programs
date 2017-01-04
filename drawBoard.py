def user_input():

    size = int(input("What size would you like the board to be? "))

    by = int(input("{} by what size would you like it to be? ".format(size)))

    print("Okay! Your board size is {}".format(size) + " X " + "{}".format(by))

    return size, by


def create(size):

    top = " ---"
    sides = "|   "

    top_row =(top*size)
    sides_row =(sides*(size +1))

    print (top_row)
    print (sides_row)
    return top_row

def multiple(size,by,top_row):
    count = 0
    while by > count:
        count = count +1
        create(size)
    print(top_row)

def main():
    size, by = user_input()
    top = " ---"
    top_row = top*size
    multiple(size,by,top_row)

main()
    



