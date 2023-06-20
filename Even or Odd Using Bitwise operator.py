#Write a program to check whether a number is even or odd using bitwise operator.
#last bit(LSB) is 0 for all even numbers and 1 for all odd numbers.
#Example : 2 - 0000 0010, 8 - 0000 1000 and 5 - 0000 0101

num=int(input("Enter a number:"))

#print("Binary representation of num is:",bin(num))
if((num&1)==0):
    print("{} is Even Number".format(num))
else:
    print("{} is Odd Number ".format(num))

#using List
num=int(input("Enter a number:"))
a=list(bin(num))
print(a)
l=''.join(a)
b=bin(num)
#type(l)
int(l[-1])
b[-1]
if int(b[-1]) ==0:
    print("{} is Even Number".format(num))
else:
    print("{} is Odd Number".format(num))
    
