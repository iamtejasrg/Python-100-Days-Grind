# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:22:50 2019

@author: Dell

"""
b=[]
a=int(input('enter nuber')) 

for i in range(0, a+1):
    if i>1:
        for num in range(2,i):
            if (i%num)==0:
                
                break
            else:
                print(i+1)
            