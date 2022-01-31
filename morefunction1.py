x =int(input("Enter number:-"))
def harshad(x):
    x1= list(str(x))
    print(x1)
    i=0
    j=i+1
    while i<len(x1) and j<len(x1):
        c=int(x1[i])+int(x1[j])
        j+=1
        i+=1
    print(c)
    if x%c==0:
        print(x,"Harshad number")
    else:
        print(x,"not Harshad")
harshad(x)
