def miniMaxSum(arr):
    arr.sort()
    min=0
    max=0
    i=0
    j=1
    while i<len(arr)-1 and j<len(arr):
        min+=arr[i]
        max+=arr[j]
        i+=1
        j+=1
    return(min,max)
print(miniMaxSum([1,3,5,7,9]))
print(miniMaxSum([17,6,30,8,9]))