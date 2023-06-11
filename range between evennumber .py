# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 07:45:42 2020

@author: Dell
"""

"Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number."

x, y = int(input("enter two value ").split())
#m=int(input('enter the number m:'))
#n=int(input('enter the number n:'))
evennumbers=[];
oddnumbers=[];
for i in range(x,y+1):
    if (i%2)==0:
        #print(i, end=', ')
        evennumbers.append(i)
    else:
        #print('odd numbers are', i , end=',')
        oddnumbers.append(i)
print('The even numbers are' ,evennumbers)
print('The odd numbers are', oddnumbers)     
        

""""
ar=[]
for i in range(1,20):
  if i%4 == 0: ar.append('four')
  elif i%6 == 0: ar.append('six')
  else: ar.append(i)
  
  x = list(map( input("Enter a multiple value: ").split())) 
print("List of students: ", x) 

 N = list(map(int, input().split())) """