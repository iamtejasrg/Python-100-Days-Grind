#Write a program to convert decimal to binary number system using bitwise operator.
def binary_2_decimal(int):
    
    ## constant = 10000000000000000000000000000000
    const = 0x80000000
    
    output = ""
    ## for each bit
    for i in range(1,33):
        
        ## if the bit is set, print 1
        if( int & const ):
            output = output + "1"
        else:
            output = output + "0"
            
        ## shift the constant using right shift
        const = const >> 1
    
    print(output)


#To use the function
binary_2_decimal(4)


x=int(input("enter the number"))
const=0x80000000 #The hexadecimal value are used for pointing to some address in memory.
#It is a hexadecimal number. In programing language, a hexadecimal number should have
# "0x" followed by hexadecimal(80000000) number.
#8|0|0|0|0|0|0|0 = 1000|0000|0000|0000|0000|0000|0000|0000

#So 0x80000000 = 0b10000000000000000000000000000000
out=''
for i in range(1,33):
    pass
    if(x&const):
        out=out+'1'
    else:
        out=out+'0'
    const=const >> 1
print(out)
len(out)


bin(const)
len('0b10000000000000000000000000000000')

x='10000000000000000000000000000000'
y='00000000000000000000000000001010'
