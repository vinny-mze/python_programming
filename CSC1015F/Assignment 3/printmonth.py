# calendar
# vince ian muzerengwa

month=input("Enter the month ('January', ..., 'December'): ")
day=input("Enter the start day ('Monday', ..., 'Sunday'): ")

print(month)
print("Mo",'Tu',"We","Th",'Fr','Sa','Su',sep=" ")

y=1
if month =="January":
 y=31
if month == "February":
 y=28
if month =="March":
  y=31
if month=="April":
  y=30
if month =="May":
  y=31
if month =="June":
  y=30
if month =="July":
  y=31
if month =="August":
  y=31
if month =="September":
  y=30
if month =="October":
  y=31
if month =="November":
  y=30
if month =="December":
  y=31


x=1
if day=='Sunday':
 x=-5
 
if day=='Monday':
  x=1
if day=='Tuesday':
  x=0 
if day=='Wednesday':
  x=1    
if day=='Thursday':
  x=-2
if day=='Friday':
  x=-3        
if day=='Saturday':
  x=-4
  


if -6<x<2:
        while x<=y:
         
        
          for column in range (6):
                  for row in range(7):
                   if x<1:
                     print("  ",end=" ")
                   elif x>y:
                 
                    break
                   else:
                    print("{:2}".format(x),end=" ")
                   x+=1    
                  print()
    
