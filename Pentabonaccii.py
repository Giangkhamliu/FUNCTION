def count_odd_pentaFib(n):
    a=0
    b=1
    c=0
    d=[]
    while c<=n:
        d.append(c)
        a=b
        b=c
        c=a+b
    c=0
    i=0
    while i<len(d):
        if d[i]%2!=0:
            c+=1
        i+=1
    return c
print(count_odd_pentaFib(5))      
    
    
    

