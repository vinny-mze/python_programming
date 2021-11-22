# CHANGE FEET TO METRES
# vince ian muzeremgwa 

a=eval(input("Enter the minimum number of inches (not less than 0):\n"))
b=eval(input("Enter the maximum number of inches (not greater than 11):\n"))

if a >  -1 and b <12:
     print("Inches: ",end = "")
     for i in range (a,b+1):
          print("{:4}".format(i),sep=" ",end=" ")
            
     print("\nMetres: ",end = "")  
     for j in range (a,b+1):
          k=j*0.0254
          #k=round(k,2)
          print("{:.2f}".format(k),sep=" ",end=" ")
          #print(k,end="  ")
 