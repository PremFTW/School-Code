#Alphabet
with open('alphabet.txt', 'r') as f:
    alphabet = f.read()

key = alphabet[::-1]
print(key)
#with open('reverse.txt', 'r') as f:
#    key = f.read()
    
#encrpyted message
with open('file_007271.txt', 'r') as f:
    encrpyted_message = f.read()

def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result

decrypted = decrypt(encrpyted_message)

#print(decrypted)
