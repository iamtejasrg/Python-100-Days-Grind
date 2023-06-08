#Write a program to compute the frequency of the words from the input.

#The output should output after sorting the key alphanumerically.

#Suppose the following input is supplied to the program:

#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

#Then, the output should be: 2:2, 3.:1, 3?:1, New:1, Python:5, Read:1, and:1, between:1, choosing:1, or:2, to:1

str1=input('enter the string:')
l=list(str1.split())
#l.sort()
l1=list(set(l)) #removes the duplicate
l1.sort()

for i in l1: 
    #print(l.count(i))
    print( "Frequency of" ,i ,'is', l.count(i)) #
    
    
    
#other method
str1=input('enter the string:')
l=str1.split()
l.sort()
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
for i in range(0,len(l2)):
    print('Frequency ',l2[i], 'is', l.count(l2[i]))
    
