with open("Sage.txt", "r") as f:
    words = f.read()

def shift(letter, shift_amount):
    unicode = ord(letter) + shift_amount

    if unicode > 126:
        unicode -= 95
        new_letter = chr(unicode)
    elif unicode < 32:
        unicode += 95
        new_letter = chr(unicode)
    else:
        new_letter = chr(unicode)

    return new_letter

def decrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, -1*shift_amount)

    return result

secret_message = words
decrypted_message = decrypt(secret_message, 26)

print(decrypted_message)
