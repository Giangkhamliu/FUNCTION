def century(year):
    a=str(year)
    b=year%100
    if len(a)==4:
        if b>=1 and b<=99:
            return int(a[:2])+1
        return int(a[:2])
    elif len(a)==3:
        if b>=1 and b<=99:
            return int(a[:1])+1
        return int(a[:1])
    elif year<100:
        return 1
print(century(1705))
print(century(1900))
print(century(1601))
print(century(356))
print(century(89))
print(century(2000))