def switcheroo(s):
    i=0
    a=""
    while i<len(s):
        if s[i]=="a":
            a+="b"
        elif s[i]=="b":
            a+="a"
        else:
            a+=s[i]
        i+=1
    return a
print(switcheroo("abc"))
print(switcheroo("aabcc"))
print(switcheroo("bbabcabb"))
print(switcheroo("aaaa"))
print(switcheroo("ccccc"))
print(switcheroo("ababababab"))