
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
        result += shift(letter, shift_amount)

    return result


def decrypt(message, shift_amount):

    return encrypt(message, -1*shift_amount)

secret_message = " PremFTW SASASKJHALKFHALIiowhlddsjkhdf12390='=Q12''/* "
encrypted_message = encrypt(secret_message, 3)
decrypted_message = decrypt(encrypted_message, 3)

print(secret_message)
print(encrypted_message)
print(decrypted_message)

