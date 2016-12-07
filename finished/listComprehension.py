#List Comprehension
#Print out even and odd numbers from the given list


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

e = []

o = []


for items in a :
    if items % 2 == 0:
        e.append(items)
    else:
        o.append(items)

print("This is the even list")
print(e)
print ('')
print("This is the odd list")
print(o)

#BOOK ANSWER - even numbers only in one line of code.

# b = [for items in a if items % 2 ==0] 
# print (b)
    
