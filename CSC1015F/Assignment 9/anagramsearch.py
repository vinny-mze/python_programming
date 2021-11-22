
  
    
    
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
   print ("***** Anagram Finder *****")
   
   try:
      f = open("EnglishWords.txt","r")
      anagram=input("Enter a word: ")
      an=[]
      
     
      #word=f.readline()
      
      #while word !="":
       #   compare= check(anagram,word)
        #  if compare== True:
         #     an.append(word)
          #word=f.readline()
      #f.close()
      for word in f :
         word=word.strip()
         compare= check(anagram,word)
         if compare:
            an.append(word)
         
      f.close()        
      #print (an)
  
      if an==[]:
          
         print ("\nSorry, anagrams of "+"'"+anagram+"'"+" could not be found.")
      else:
         print("\n"+ str(an))
      return an
    
   except: 
      print("Sorry, could not find file 'EnglishWords.txt'.")
    
    
   
    
    
main()