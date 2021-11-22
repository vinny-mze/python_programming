# GUMATJ LANGUAGE
# VINCE IAN MUZERENGWA


def gumatj_to_decimal(a):
    
    if a <5:
        num=a
    else:
        num=(int(str(a)[0])*5)+int(str(a)[1])
    if a ==0:
        num=0
       
    
    return num

def decimal_to_gumatj(a):
    x=""
    while a!=0:
        k=str(a%5)
        x+=k
        a=int(a/5)
    x=x[::-1]
    if a ==0:
        x=0    
    return x

def gumatj_add(a,b):
    if a <5:
        num1=a
    else:
        num1=(int(str(a)[0])*5)+int(str(a)[1])
    if b <5:
        num2=b
    else:
        num2=(int(str(b)[0])*5)+int(str(b)[1])
        
    total=num1+num2
    
    x=""
    while total!=0:
        k=str(total%5)
        x+=k
        total=int(total/5)
    x=x[::-1]  
    if a ==0 and b == 0:
        x=0
    
    return x

def gumatj_multiply(a,b):
    
    if a <5:
        num1=a
    else:
        num1=(int(str(a)[0])*5)+int(str(a)[1])    
        
    if b <5:
        num2=b
    else:
        num2=(int(str(b)[0])*5)+int(str(b)[1])    
    

    y=num1*num2
    
    x=""
    while y!=0:
        k=str(y%5)
        x+=k
        y=int(y/5)
    x=x[::-1]
    if a ==0 and b == 0:
        x=0    
    
    return x