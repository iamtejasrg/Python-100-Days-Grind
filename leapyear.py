#leap year 
#These are the conditions for the leap year
#The year is evenly divisible by 4;
#If the year can be evenly divided by 100, it is NOT a leap year, unless;
#The year is also evenly divisible by 400. Then it is a leap year.

year=int(input("Enter the year: "))
if (year%4 == 0 and year%100 != 0 or year % 400 == 0):
    print(year,"is Leap year")
else:
     print(year,"is not Leap year")
     
     
# using the Functinon
year=int(input("Enter the year: "))
def Is_Leapyear(year):
   if (year%4 == 0 and year%100 != 0 or year % 400 == 0):
    print(year,"is Leap year")
   else:
     print(year,"is not Leap year")
Is_Leapyear(year)


#using Multiple If Statements
year=int(input("Enter the year: "))
if(year %4==0) :
    print(year,"is a leap year")
elif(year%100==0) and (year%400):
    print(year,"is a leap year")
else:
    print(year,"is a not leap year")
    
    
    
