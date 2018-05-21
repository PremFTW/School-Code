#Open the file
with open("file_010005.txt", "r") as f:
    words = f.read()

#Inserting all of the character count into array
def Char_count():
    charcount = [0] * 127
    for w in words:
        n = ord(w)
        charcount[n] += 1
    counts = charcount[32:127]

    return counts

#Finding the Average
def mean(counts):
    avg = sum(counts) / len(counts)

    return avg

#Chi-Square
def Chi_Sqaure(counts):
    exp = mean(counts)
    x = 0
    for w in counts:
        x += (w - exp)**2

    return x / exp
counts = Char_count()
print(Chi_Sqaure(counts))

