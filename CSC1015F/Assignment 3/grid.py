# grid
# vince ian muzerengwa

num=eval(input("Enter the start number: "))

numcpy=num+41

if -6<num<2:
        while num<numcpy:
        
                for column in range (6):
                        for row in range(7):
                                print("{:2}".format(num),end=" ")
                                num+=1
                               
                        print()