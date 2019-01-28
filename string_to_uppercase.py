G = "I am Zorawar Singh"
print(G.split())
from string import punctuation
def patern(word):
   
    clean = ''
    for patern in word:
        if ((patern in punctuation)):
            pass
        else:
            clean += patern.lower()            
    return(clean)
print(patern(G ))
