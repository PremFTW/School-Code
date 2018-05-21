
##############################################################################################
    
#Alphabet
with open('alphabet.txt', 'r') as f:
    alphabet = f.read()

#keycode
with open('reverse.txt', 'r') as f:
    key = f.read()

#encrpyted message
with open('file_007271.txt', 'r') as f:
    unencrpyted_message = f.read()
    
#Hiding the message
def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

#Returning back to the original message
def decrypt(message):
    origin =  ""

    for letter in message:
        loc = key.find(letter)
        origin += alphabet[loc]

    return origin



encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)


print(decrypted_message)
