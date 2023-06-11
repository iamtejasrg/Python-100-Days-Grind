z='ababcdacdabdaeqjifarhthyudbbbbaaaadddeeechsyaaa'
str1=""
for i in z:
    if i not in str1:
        if z.count(i)!=1:
            str1=str1+i
        else:
            str1=str1+i
print(str1)


z='ababcdacdabdaeqjifarhthyudbbbbaaaadddeeechsyaaa'
z.replace('a','')


z='ababcdacdabdaeqjifarhthyudbbbbaaaadddeeechsyaaa'
str1=""
while True:
    for i in z:
        z=z.replace(i,"")
        str1=str1+i
        print(z) # for understanding purpose i wrote z here
        break
    else:
         break
print(str1)
len(str1)
print(z)
len(z)
type(z)

z='ababcdacdabdaeqjifarhthyudbbbbaaaadddeeechsyaaa'
str1=""
for i in z:
    if i not in str1:
        z=z.replace(i,"")
        str1=str1+i
print(str1)

z='ababcdacdabdaeqjifarhthyudbbbbaaaadddeeechsyaaa'
str1=""
for i in z:
    if i not in str1:
        #z=z.replace(i,"")
        str1=str1+i
print(str1)
    
    
z=" a b "
a=""
for i in z:
    a=a+i
print(a)
  
    

air="abaaacbbbd"
count=0
for i in range(len(air)):
    air=air.replace(air[i],"") #i can't update ,air will update
    count=count+1
    print(air)
    #break
print(count)
        

d1={'a':2}
d2={'a':3}

d1>d2
d1['b']


a={1,2,3}
b={2,3,4}
a.update([1,2])
len(a)
type({})

len(a+b)

