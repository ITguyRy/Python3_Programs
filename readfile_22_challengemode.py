def read():
    counter_dict = {}
    with open('image_database.txt','r') as database:

        text = database.readline()
        while text:
            text = text[3:-26]
            if text in counter_dict:
                counter_dict[text] +=1
            else:
                counter_dict[text] = 1
            text = database.readline()
    print('\n'.join(counter_dict))





def main():

    read()


main()
