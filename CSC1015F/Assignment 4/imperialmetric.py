# imperial metric
#vince ian muzerengwa

a=eval(input("Enter the minimum number of feet (not less than 0):\n"))
b=eval(input("Enter the maximum number of feet (not more than 30):\n"))

if a>-1 and b < 31:
    print("\n  ","   |",end = "  ")
    for i in range(0,12,1):
        print('{:2}"'.format(i),end = "  ")
    print()
    while a < b:
        for j in range(a,b+1):
            print("","{:3}'".format(j),'|',end ="")
            
            for k in range(12):
                num =a*0.3048
                print("","{:.2f}".format(num),end = "")
                a = a + (1/12)
            print()
                
        

