def list_one():

    with open('happynumbers.txt','r') as happy:
        happylist = []
        output = happy.read().split('\n')

        happylist.append(output)

        for i in happylist:
            happylists = list(map(int,i))

    return happylists


def list_two():

    with open('primenumbers.txt','r') as prime:
        primelist = []

        output = prime.read().split('\n')

        primelist.append(output)

        for i in primelist:
            primelists = list(map(int,i))

    return primelists


def overlap(happylists,primelists):
    commonlist = []
    for elements in happylists:
        if elements in primelists:
            commonlist.append(elements)
    print (commonlist)
            
        

def main():
    happylists = list_one()
    primelists = list_two()
    overlap(happylists,primelists)

main()




    
