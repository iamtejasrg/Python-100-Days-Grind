# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:10:48 2020

@author: Dell
"""

#"Write a program that accepts a sentence and calculate the number of letters and digits.
'Suppose the following input is supplied to the program:'
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3"
list=input('enter the string :')
Letters=0;
Degits=0;
Spaces=0;
Special_Characters=0;
for p in list:
    if(p.isalpha()):
         Letters=Letters+1;
    elif(p.isnumeric()):
         Degits=Degits+1;
    elif(p.isspace()):
       Spaces=Spaces+1;
    else:
       Special_Characters=Special_Characters+1;
        
print("The No of Letters is ",Letters)
print("The No of Degits is",Degits)
print("The No of Spaces is" , Spaces)
print("The No of SP is",Special_Characters)


    
   