'''
1. How many total words are in the list?
2. How many words are exactly 5 letters long?
3. How many words in the dictionary are over 7 letters long?
4. What is the total number of characters used in all words?
5. How many words do not contain the letter E?
6. How many words begin and end with the same letter?
7. How many words contain exactly 3 As?
8. How many words contain a Q that is not followed by a U?
(Be sure you check followedor Qs that aren't the first letter in the word too.)
'''
#count all the chracters
with open("words_alpha.txt" , "r") as f:
    words = f.read()
count = len(words)
print(count)

#opening the file
with open("words_alpha.txt" , "r") as f:
    words = f.read().splitlines()
#print some words from there
print(words[:5])

#counting all of the words in the file  
count = 0
for w in words:
    if len(w) > 0:
        count += 1
print(count)

#counting all the words that have exactly 5 letters in the file
count = 0
for w in words:
    if len(w) == 5:
        count += 1
print(count)

#counting all the words that have more than 7 letter
count = 0
for w in words:
    if len(w) > 7:
        count += 1
print(count)

#counting all the words that end with the same letter they begin with
count = 0
for w in words:
    if w[0] == w[-1]:
        count += 1
print(count)

#counting all the words that don't have the letter "E"
count = 0
for w in words:
    if "e" in w:
        count += 1
print(count)

#counting all the words with exactly 3 A's
count = 0
for w in words:
    acount = 0
    for letter in w:
        if letter == "a":
            acount += 1
    if acount == 3:
        count += 1
print(count)

#counting all the words with Q's not followed by U's     
count = 0
for w in words:
    for i in range(len(w)):
        if w[i] == w[i+1]:
            count += 1
print(count)







      
