def find (num):
    f=open ("EnglishWords.txt","r")
    word=f.read()
    
    for anagram in str.split(word):
        if len(anagram)==num:
            return anagram
        
        search(anagram)
        #f.close()
        
def search(anagram):
    
    f = open("EnglishWords.txt","r")
    an=[] 
    for word in f :
        word=word.strip()
        compare= check(anagram,word)
        if compare:
            an.append(word)
            print (an)
        f.close()
        
def check(anagram,word):
    if word == anagram:
        return False
    x=list(anagram)
    y=list(word)

    x.sort()
    y.sort()
   
    if x==y:

        return True
    else:
        return False 
   
def main():
    num=eval(input("Enter word length:\n"))
    
    find(num)
    
main()    