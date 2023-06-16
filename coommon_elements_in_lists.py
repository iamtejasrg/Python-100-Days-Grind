#find elements in common lists
l1=[1,2,3,4,5]
l2=[2,5,6,7,8]

count=0
for i in l1:
    for j in l2:
        if i==j:
            print(i)
            count=count+1
print('the number of common elements',count)

#randomly choose l1 and l2
import random
l1=list(range(100))
random.shuffle(l1)
l2=list(range(50))
random.shuffle(l2)

count=0
for i in l1:
    for j in l2:
        if i==j:
            print(i,end='.')
            count=count+1
            
print('\nThe number of common elements',count)

#using dictinary
#property of dictinary is time complexity is less order(1)
import random
l1=list(range(100))
random.shuffle(l1)
l2=list(range(50))
random.shuffle(l2)

d={}
for ele in l2:
    d[ele] = 1;
    
count=0
for i in l1:
    if d.get(i)!=None:
        print(i,end=',')
        count=count+1
        
print('\nNumber of common elements:',count)



    
