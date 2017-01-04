def file_name():

    filename = input("What is the name of the file you want to read from? (namelist.txt)")

    return filename


def read_from():

    with open('namelist.txt','r') as open_file:
        names = []
        line = open_file.readline()
        while line:
            line = open_file.readline().strip('\n')
            for name in line:
                names.append(line)
                
    names = set(names)
    
    name_len = (len(names))

    print("There are {} names in this file. \n".format(name_len) +'{}'.format(', '.join(names)) )
    

        
        


def main():

    #filename = file_name()
    read_from()

main()
