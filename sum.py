#Add the two numbers with map functions
'enter the inputs'
numArray=map(int, input('enter the numbers,').split())
sum=0
for imjjsk in numArray:
    'logic'
    sum+=imjjsk
print(sum)


def sum( *a,b):
    l=0;
    for i in range(0,len(a)):
        l +=a[i]; 
        sum= l + b;
        return sum
       
sum(2,31,22)
