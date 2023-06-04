import math

def binary_search(arr,l,r,x):
    
    #check the base case
    if r>=1:
        
        mid=1+math.floor((r-l)/2)
        
        #if element present in the middle
        if arr[mid]==x:
            return mid
        
        #if the element is smaller than mid it can present left side of the mid
        elif arr[mid]>x:
            return(binary_search(arr,l,mid-1,x))
            
        #else it will present only right side of the array
        else:
            return(binary_search(arr,r,mid+1,x))
    
    #element not present in array
    else:
        return 'its not present'

l=[10,20,30,40,5,6,7,8]    
l.sort()
arr=l;
q=6;
binary_search(arr,0,len(arr)-1,q)
    
        
            