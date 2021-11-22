# CHANGE INCHES TO METRES
# vince ian muzeremgwa 

a=eval(input("Enter the minimum number of feet (not less than 0):\n"))
b=eval(input("Enter the maximum number of feet (not more than 99):\n"))

if a>  -1 and b <101:
        
        for j in range(a,b+1,1):
                k=j*0.3047
                #k=round(k,2)
                
                
                
                print("  {0:2}'".format(j),"|  ","{:.2f}".format(k),end="m\n")
        
    

    