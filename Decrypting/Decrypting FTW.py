with open("Encryptedmessage.txt", "r") as f:
    words = f.read().splitlines()

count = len(words)
print(count)
