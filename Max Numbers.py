#write the program to find the Maximum of three numbers
#using only conditional operator

a=int(input('Enter the First Number :'))
b=int(input('Enter the second Number :'))
c=int(input('Enter the Third Number :'))

if (a>=b) and (a>=c):
    print(a,"is Maximum Number")
elif (b>=a) and (b>=c):
    print(b,"is Maximum Number")
else:
    print(c,"is Maximum Number")
    
   