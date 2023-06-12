""""You are required to write a program to sort the (name, age, height) tuples by ascending order 
where name is string, age and height are numbers."""

#The tuples are input by console. The sort criteria is:

#1: Sort based on name;

#2: Then sort based on age;

#3: Then sort by score.

#The priority is that name > age > score.

#If the following tuples are given as input to the program:

#Tom,19,80

#John,20,90

#Jony,17,91

#Jony,17,93

#Json,21,85

#Then, the output of the program should be:

#[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

l1=[('tom',19,80),('Jhon',20,90),('Jony',17,93),('Jony',17,91),('json',21,85)]
l2=[]
l3=[]
l4=[]
for i in l1:
    l2.append(i[0])
    l3.append(i[1])
    l4.append(i[2])
l2=list(set(l2))
l3=list(set(l3))
l4=list(set(l4))
l2.sort()
l3.sort()
l4.sort()
for x in l2:
    for y in l3:
        for z in l4:
            for i in l1:
                if x==i[0] and y==i[1] and z==i[2]:
                    print(i)
                    
                    
                    
