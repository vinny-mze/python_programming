def palindrome(s,mid,x):
    if mid >=-(len(s)):
        x.append(s[mid])
        mid=mid-1
        palindrome(s,mid,x)
    return x

def array(s,i,y):
    if i < len(s):
        y.append(s[i])
        i=i+1
        array(s,i,y)
    return y
    
   
        
def main ():
    s=input("Enter a string:\n")
    x= []
    y=[]
    mid = -1
    i=0
    palindrome(s,mid,x)
    array(s,i,y)
    if y==x:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
 
main()
        
        
    