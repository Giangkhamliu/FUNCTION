def index(array, n):
    if n>=len(array):
        return -1
    else:
        a=array[n]**n
        return a
print(index([1,3,10,100],3))
print(index([1,2,3,4],2))
print(index([1,3,10,100],4))