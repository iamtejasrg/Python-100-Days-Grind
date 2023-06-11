n=int(input())
m=n*3
x='WELCOME'
y='.|.'

for i in range(1,n,2):
    print(y.center(m,'-'))





N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(0,N//2): 
    print (('.|.'*i).rjust((M-2)//2,'-')+'.|.'+('.|.'*i).ljust((M-2)//2,'-'))
print ('WELCOME'.center(M,'-'))
for i in reversed(range(0,N//2)): 
    print (('.|.'*i).rjust((M-2)//2,'-')+'.|.'+('.|.'*i).ljust((M-2)//2,'-'))
    
    

N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(0,N//2): 
    print ((y*i).rjust((M-2)//2,'-')+y+(y*i).ljust((M-2)//2,'-'))
print (x.center(M,'-'))
for i in reversed(range(0,N//2)): 
    print ((y*i).rjust((M-2)//2,'-')+y+(y*i).ljust((M-2)//2,'-'))
    
    
    
    
N,M=map(int,input().split())
x='-|-'
y='WELCOME'
for i in range(0,N//2):
    print((x*i).rjust((M-2)//2,'-')+x+(x*i).ljust((M-2)//2,'-'))
print(y.center(M,'-'))
for i in reversed(range(0,N//2)):
    print((x*i).rjust((M-2)//2,'-')+x+(x*i).ljust((M-2)//2,'-'))
    
    
    
    
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print(i, oct(i),format(hex(i)),bin(i))
        h=hex(i)
        format(h)
        
print_formatted(21)
#import pdb
n = int(input())
w = len("{0:b}".format(n))
#pdb.set_trace()
for i in range(1,n+1):
  #pdb.set_trace()
  print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
  #pdb.set_trace()

len("{0:b}".format(n))

c=('{0:{width}d}'.format(1,width=0))
c



