def strings_xor(s,t):
    res=""
    for i in range(len(s)):
        if s[i]==t[i]:
            res=res+'0'
        else:
            res=res+'1'
    return res
s = input("Enter the no.=")
t = input("Enter the no.=")
print(strings_xor(s, t))



