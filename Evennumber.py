# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 04:05:57 2019

@author: Dell
"""
#find the even number
'''"Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit 
of the number is an even numberThe numbers obtaine should be printed in a comma-separated sequence 
on a single line."'''
count=0;
for i in range(1000,3001):
    if (i%4000==0):
        count=count+1;
        print(i)
    else:
        count=count+1;
        print(i+1)
print(count)

count=0;
[x for x in range(1000,3000) if x%200==0]
count=count+1;
print(count)

#count the letters and degits
'''"Write a program that accepts a sentence and calculate the number of letters and digits
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"'''
Degit=[0,1,2,3,4,5,6,7,8,9]
m=1,2,3 
n='hello123'
for i in m:
    if i==Degit:
        count=count+1;
        print('love')
print(count)
type('s')
Degit=[0,1,2,3,4,5,6,7,8,9]
