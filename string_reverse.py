def string(s):
    str1 = ''
    i= len(s)
    while i> 0:
        str1 += s[i-1]
        i= i-1
    return str1
s=input("Enter the string:-")
print(string(s))
