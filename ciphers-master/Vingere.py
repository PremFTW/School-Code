
#Alphabet
with open("alphabet.txt", "r") as f:
    alpha = f.read
#key
key ="enigma"

#read the thing i need to solve
with open("file_012499.txt", "r") as f:
    encrpyted_message = f.read()

def decrpyt(message):
    result = ""

    count = 0
    for letter in message:
        keynum = ord(key[count % 6])
        letternum = ord(letter[count])
        new_number = keynum - letternum
        
        if new_number > 126:
            new_number -= 95
        elif new_number < 32:
            new_number += 95

        new_letter = chr(new_number)
        result += new_letter
        count += 1
        
    return result


decrypted = decrpyt(encrpyted_message)
print(decrypted)
