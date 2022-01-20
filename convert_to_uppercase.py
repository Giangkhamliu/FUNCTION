def str():
    str=input("Enter the Lower case):")
    i=0
    ch=''
    while len(str)>i:
        if str[i]>='a' and str[i]<='z' :
            ch+=chr(ord(str[i])-32)
        else:
            ch += chr(ord(str[i]))
        i+=1
    print("upper case String is:", ch)
str()
