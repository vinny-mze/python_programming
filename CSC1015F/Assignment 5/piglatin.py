# translate english to latin
# vince ian muzerengwa

def to_pig_latin (sentence):
    x=sentence.split()
    y=x[0]
    
    #count=0
    for i in range(len(x)):
        y=x[i]
        
        
        if y[0] in ["a" , "e" , "i" , "o" , "u"]:
            x[i]= y+"way"
            
        elif y[1] in ["a" , "e" , "i" , "o" , "u"]:
            x[i]=y[1:]+"a"+y[:1]+"ay"
            #x[i]=y[2:]+y[:2]+"ay"
            
        else:
            x[i]=y[2:]+"a"+y[:2]+"ay"
            
        c=" ".join(x)
            #x[i] = y[1:]+[0]+'ay'    
            
                #count+=1
            
    return  c  
        
def to_english(sentence):
    x=sentence.split()
    word = ""
    for i in x:
        if i[:len(i) - 4:-1] == "yaw":
            word += i[:len(i) - 3] + " "
        else: 
            a = i[:len(i) - 2]
            b = a.split("a")[-1]
            c = a[:len(a) - (len(b)+1)]
            word += b + c + " "    
   
    return  word      
    
            
    
    
        
        
        
    