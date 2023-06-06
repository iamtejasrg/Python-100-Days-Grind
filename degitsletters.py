# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:40:42 2020

@author: Dell
"""
#calulate the number of letters and degits''

list=input("enter string:")
letters=0
numbers=0
for i in list:
    if (i.isalpha()):
        letters=letters+1
    else:
        numbers=numbers+1
        
print(letters)
print(numbers)

# for two numbers input
num3,num1, num2 =map(int, input().split())
sum=num1+num2+num3
print (sum)

numArray = map(int, input('enter the numbers ,').split()) # Get the input


sum_integer = 0
# write your logic to add these 4 numbers here

for number in numArray:
    sum_integer += number
print(sum_integer) # Print the sum
x, y = input("Enter a two value: ").split()
print(x+y)