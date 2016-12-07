##Program Description: This program will calculate a person's gross weekly pay.

def load():
    wageH = float(input("Enter your hourly wage: "))
    hoursW = int(input("Enter the amount of hours worked: "))
    return wageH, hoursW

def pay(wageH, hoursW):
    if hoursW > 40:
        overTimePay = wageH * 1.5
        overTime = (hoursW - 40) * overTimePay
        #need to reset hours back to base
        hoursW = 40
    else:
        overTime = 0
    
    weeklyP = (wageH * hoursW) + overTime

    return weeklyP

def output(weeklyP):
    print("Your gross weekly pay is: $",format(weeklyP, '.2f'))

def main():
    wageH, hoursW = load()
    weeklyP = pay(wageH, hoursW)
    output(weeklyP)

main()

##Enter your hourly wage: 10
##Enter the amount of hours worked: 44
##Your gross weekly pay is: $ 460.00
##>>> 
##
##Enter your hourly wage: 10
##Enter the amount of hours worked: 40
##Your gross weekly pay is: $ 400.00
##>>> 
