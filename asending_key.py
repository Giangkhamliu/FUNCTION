a=[('a',1),('b',4),('z',7),('y',2),('i',5),('j',3),('o',6)]
i=0
b=[]
c1=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        a1=a[i][1]
        b.append(a1)
        b.sort()
        k=0
        while k<len(b):
            if b[k]==a[i][1]:
               c=a[i]
               
            k+=1
        j+=1
    i+=1
    c1.append(c)
print(c1)