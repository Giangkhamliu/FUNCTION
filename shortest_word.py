def find_short(s):
    a=[]
    b=s.split()
    i=0
    while i<len(b):
        j=0
        c=0
        while j<len(b[i]):
            c+=1
            j+=1
        a.append(c)
        a.sort()
        i+=1
    return a[0]
print(find_short("Let's travel abroad shall we")) 
print(find_short("turns out random test cases are easier than writing out basic ones"))
print(find_short("Lets all go on holiday somewhere very cold"))

