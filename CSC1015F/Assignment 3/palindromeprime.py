# palindrome prime
# vince ian muzerengwa


start=eval(input("Enter the start point N:\n"))
stop=eval(input("Enter the end point M:\n"))
print("The palindromic primes are:")

for prime in range(start+1,stop):       
    digit=0
    for num in range (2,prime//start+stop):
        x = prime%num
        if x==0:
            digit = digit +1

    if digit<2:
        prime = str(prime)
        palin= prime[::-1]
    
        if prime==palin:
            print(prime)
        