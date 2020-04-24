from srt_normalizer import *
  
def findWord(word, list):
    count = 0
    for s in list:
        count = count+1
        if s.find(word) !=-1 : #si on trouve le mot
            return count
    return -1


normalize("sw3.srt")
file1 = open('sw3.txt', 'r') 
Lines = file1.readlines() 
quotes = [""]*len(Lines)
timeStamp = [""]*len(Lines)
count = 0 
i=0
#on parcourt tutes les lignes 
while i<len(Lines)-5 :
    #la premiere ligne c'est le numéro du sous titre, on s'en cogne
    i=i+1
    #on save le timestamp
    timeStamp[count]=Lines[i]
    i=i+1
    #maintenant on save le texte
    s=""
    while Lines[i] != "\n" :
        s2=Lines[i].replace("\n", " ") 
        s=s+s2
        i=i+1
    quotes[count]=s
    i=i+1
    count=count+1
    #et on recommence

print(findWord("clones", quotes))

