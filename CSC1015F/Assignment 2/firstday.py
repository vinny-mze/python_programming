# first day
# vince ian muzerengwa

first=eval(input("Enter the first year:\n"))
second=eval(input("Enter the second year:\n"))


for i in range(first,second+1,1):
    
    a = 5*((i-1)%4)
    b = 4*((i-1)%100)
    c = 6*((i-1)%400)
    day = ((1+a+b+c)%7)   
    
    if day ==0:
        print("The 1st of January",i,"falls on a Sunday.")
    if day==1:
        print("The 1st of January",i,"falls on a Monday.")
    if day==2:
        print("The 1st of January",i,"falls on a Tuesday.")
    if day==3:
        print("The 1st of January",i,"falls on a Wednesday.")
    if day==4:
        print("The 1st of January",i,"falls on a Thursday.")
    if day==5:
        print("The 1st of January",i,"falls on a Friday.") 
    if day==6:
        print("The 1st of January",i,"falls on a Saturday.")
