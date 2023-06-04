#check the Given string is Alphabet or not
#using Conditional operator
#ASCII 65-90 = Upper case(A-Z)
#ASCII 97-122= lower case (a-z)

char=input('Enter the character : ')
if ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122:
    print(char,"is Alphabetic")
else:
    print(char,"is not Alphabetic")


#using isalpha() function
char=input('Enter the Character:')
if char.isalpha():                  #65 to 90 Upper case
                                    #97 to 122 lower case
    print(char,"is Alphabetic")
else:
    print(char,"is Not Alphabetic")
    
#using the While loop
while True:
    char=input('Enter the One Character:')
    if len(char)==1:
        if ord(char)>=65 and ord(char)<=90 or ord(char)>=97 and ord(char)<=122:
            print(char,"is Alphabetic")
        else:
            print(char,"is not Alphabetic")
        break
    else:
        print("It is more than one Character enter one character")
        continue
    
#using loop             
while True:
    char=input('Enter the One Character:')
    if len(char)==1:
        if (char)>='A' and (char)<='Z' or (char)>='a' and (char)<='z':
            print(char,"is Alphabetic")
        else:
            print(char,"is not Alphabetic")
        break
    else:
        print("It is more than one Character enter one character")
        continue    
    
    
import re
char=input('enter the character :')
y=re.findall("[a-z A-Z]",char)
print(y)
if y:
   print('it is an Alphabet')
else:
   print('it is not Alphabet')