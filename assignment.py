# -*- coding: utf-8 -*-7
"""
Created on Tue Feb  4 11:53:35 2020

@author: Dell
"""

string="abc 2k 23love you 143"
b=[]
c=[]
for i in string:
    #l=string.split()
   # print (i)
    #if i.isnumeric():
        #print(i ,end="")
    if (i.isnumeric()):
        #print(i)
        c.append(i)
    else:
       # print(i)
        b.append(i)
        c.append(" ")
print(b)
d=""
str1="".join(b)

e=""
str2=e.join(c)

print('the string without albhabets are "{}",the string without numericals are "{}"'.format(str1,str2))

c="a     b    c  2 4                5  6"
c=["1","2"," "," ","4"]
a=c.split(" ")
print(a)
print("".join(c))
string=" abc 2k 23love you 143"
for i in string:
    print(i)
    l=i.split()
    c=str(l)
    if (c.isalpha()):
        print(c)
    else:
        (c.isdigit())
        print(c)

                                                                
list1=["i love",  "143","y","o","u","143you"]
list2=[]

list3=[]
for i in list1:
    for j in i:
        if j.isnumeric():
            if j not in list2:
                list2.append(j)
        else:
           list3.append(j)
    list3.append(" ")
    s=''.join(list3)
p=s.replace('youyou', ' you',1)           
    
print(list2)
str1="".join(list2)
print(str1)

print(list3)
a="".join(list3)
a=a.split(" ")
"".join(a)
