'''
Loc Testing code:
'''
import time

#Hardcoding:
word_size = 7
letters = {'l','a','u','d','o','b','b','l','r','b','e','j'}
#word_size = 5
#letters = "ilsdtodlcnuk"

#1. Read file from dictionary text & Make a DICTIONARY type base on word size
f = open('English.txt')
dictionary = dict()
for line in f:
    line = line.strip('\n') #get rid of \n at the end of line
    if dictionary.has_key(len(line)):        
        dictionary[len(line)].append(line)
    else:
        dictionary[len(line)] = [line]  #add list, the line in [] is important
#print dictionary[2]
    
       
#2. Go through the DICTIONARY with same word size, check if the word has
#the characters in letters list
possible_words = []
for word in dictionary[word_size]:
    for letter in word:
        if letter not in letters:
            #print (letter + " is not in " + word + "-> breaking")
            #time.sleep(0.1)
            correct = False
            break
        else:            
            correct = True 
            #print (letter + " is in " + word)
            #time.sleep(0.1)
    if (correct):
        possible_words.append(word) 
print possible_words
