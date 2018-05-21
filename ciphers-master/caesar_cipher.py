
def shift(letter, shift_amount):
    
    if letter == [ "|", "}", "~"]:
        return letter
    
    else:
        unicode = ord(letter) + shift_amount
        new_letter = chr(unicode)

    return new_letter

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, -1*shift_amount)

    return result


def decrypt(message, shift_amount):

    return encrypt(message, -1*shift_amount)

    
with open("Sage.txt", "r") as f:
    words = f.read()
    
secret_message = words
encrypted_message = encrypt(secret_message, 26)
decrypted_message = decrypt(encrypted_message, 26)

print(secret_message)
print(encrypted_message)

