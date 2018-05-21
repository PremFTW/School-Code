

def alphabet_write(start_vaule, end_vaule):

    count = 128
    alphabet = ""
        
    if start_vaule >= 128:
        return "You need to enter a start vaule thats less than 127"
    elif end_vaule >= 128:
        return "you need to enter a end vaule thats less than or equal to 127"
    elif start_vaule == end_vaule:
        return "You can have the start and end vaules! Enter something else"
    else:
        for number in range(count):
            alphabet += chr(number)

    return alphabet[start_vaule:end_vaule]


alpha_write = alphabet_write(32, 127)
print(alpha_write)

print(alpha_write[::-1])

with open("reverse.txt", "w") as f:
    f.write(alpha_write[::-1])
