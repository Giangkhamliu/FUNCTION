def Initials(name):
    if (len(name) == 0):
        return
    words= name.split(" ")
    print(words)
    for word in words:
        print(word[0].upper()+".",end=" ")
name = "giang grace pamei"
Initials(name)
