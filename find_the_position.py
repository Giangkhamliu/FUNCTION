def position(alphabet):
    alpha="abcdefghijklmnopqrstuvwxyz"
    i=0
    while i<len(alpha):
        if alphabet==alpha[i]:
            res=i+1
        i+=1
    return "Position of alphabet: "+str(res)
print(position("b"))
print(position("d"))
print(position("g"))
print(position("x"))
print(position("j"))