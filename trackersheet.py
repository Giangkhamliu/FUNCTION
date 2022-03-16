number=[3,5,7,34,2,89,2,5]
lar=0
i=0
while i<len(number):
    if number[i]>lar:
        lar=number[i]
    i+=1
print(lar)