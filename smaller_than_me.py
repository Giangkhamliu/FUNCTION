def smaller(arr):
    a=[]
    i=0
    while i<len(arr):
        a1=arr[i]-1
        a.append(a1)
        i+=1
    return a
print(smaller([1,3,5,3]))
print(smaller([1,2,3,4,5,6]))
print(smaller([6,4,2,7,57,2]))