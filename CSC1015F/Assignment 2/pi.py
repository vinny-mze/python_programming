# calcuting the area
# vince ian muzerengwa


a=2
b=2**0.5
c=a
pi=c

while c > 1:
    c=a/b
    b= ((a+b)**0.5)
    pi= pi * c
    
    picpy=round(pi,3) 
print("Approximation of pi:",picpy)

radius=eval(input("Enter the radius:"))

area=pi*radius*radius

area=round(area,3)

print("\nArea:",area)