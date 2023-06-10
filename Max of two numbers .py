#Find Maximum of Two number with & without using Conditional operator
#using conditional operator
a=int(input('Enter the First Number:'))
b=int(input('Enter the Second Number:'))
if a>=b:
    print(a,'is Maximum')
else:
    print(b,"is Maximum")
    

#using Max function
a=int(input('Enter the First Number:'))
b=int(input('Enter the Second Number:'))
print(max(a,b),"is Maximum Number")