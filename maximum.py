list1=[2,3,4,6,7,9]
def maximum(a):
    i=0
    n=0
    while i<len(a):
        if a[i]>n:
            n=a[i]
        i=i+1
    print(n)
maximum(list1)