user=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def show():
    a=0
    b=1
    c=0
    while c<=n:
        print(c,(user[c]))
        a=b
        b=c
        c=a+b
n=int(input("enter the number:-"))
show()
