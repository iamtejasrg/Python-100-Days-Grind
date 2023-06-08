#To find the HCF of the Two numbers

def HCF(a,b):
    """computing the HCF of two numbers"""
    smaller=b if a>b else a
    HCF=1
    for i in range(1,smaller+1):
        if (a%i==0) and (b%i==0):
            HCF=i
    return HCF

a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))        

print("H.C.F of {0} and {1} is :{2}".format(a,b, HCF(a,b)))


def gcd(x,y):
    while(y):
        x,y=y,x%y
        return  x

gcd (4,3)


