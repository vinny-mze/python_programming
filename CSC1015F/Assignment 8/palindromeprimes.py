import sys
sys.setrecursionlimit (30000)

def prime(n,a,x):
    if a <= n:
        if n%a == 0 :
            a +=1
            x.append(a)
            prime(n,a,x) 
        else:   
            a +=1
            prime(n,a,x)            
    return x  
        
def increment_x(n,m):
    #print(n)
    a=1
    x=[]
    i = 1
    count =0    
    prime(n,a,x)
    if len(x)-1< 2:
        #print(n)
        p = str(n)
        palin= p[::-1]
    
        if p==palin:
            print(n)
            
       
    if n<=m:
        n+=1
        increment_x(n,m-1)
def main():
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    increment_x(n,m-1)  
    
main()
