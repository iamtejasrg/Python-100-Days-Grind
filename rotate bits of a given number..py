#Write a program to rotate bits of a given number.
x=int(input('Enter the number:'))
y=bin(x)
y=list(y[2:])
print(y)
z=int(input("Enter the number of rotations: "))
for i in range(1,z+1):
    a=y.pop(0)
    y.append(a)
    #print("num of rotations is",i)
    print(y)
    print(''.join(y))




