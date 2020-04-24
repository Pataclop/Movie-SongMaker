from srt_normalizer import *
  
L = ["Geeks\n", "for\n", "Geeks\n"] 
  

#comment qu'on fait
# on va faire deux tableaux. un avec les timestamp, un avec le texte. chauqe case correspont au numéro du sous titre. 
# on parcourt les textes jusqu'à trouver le mot que l'on veut. quand on le trouve, on print la case. bien. 
# Using readlines() 
normalize("sw3.srt")
file1 = open('sw3.txt', 'r') 
Lines = file1.readlines() 
for l in Lines:
    print(l)

# Strips the newline character 
#for line in Lines: 
#    print(line.strip()) 
#    print("Line{}: {}".format(count, line.strip())) 
