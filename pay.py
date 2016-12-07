
hours = int(input("How many hours did you work this week? "))
if hours > 40:
    overhour = hours - 40
    print('you worked {} hours overtime'.format(overhour))


wage = float(input("What is your hourly wage? "))


print(overhour)





 

def weeklypay(hours,wage,overhour) :
    
    overtime = overhour *(1.5 * wage)

    base = hours * wage
    
    amount = base + overtime
    print ("Weekly base earned: {}".format(base))
    print ("Overtime money: {}".format(overtime))
    print ("Total week earned: {}".format(amount))


weeklypay(hours, wage,overhour)




