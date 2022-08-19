def plusMinus(arr):
    # Write your code here
    p=0
    n=0
    z=0
    i=0
    while i<len(arr):
        if arr[i]>=1:
            p+=1
        elif arr[i]<1 and arr[i]!=0:
            n+=1
        else:
            z+=1
        i+=1
    p1=p/len(arr)
    n1=n/len(arr)
    z1=z/len(arr)
    print(p1)
    print(n1)
    print(z1)
plusMinus([1,1,0,-1,-1]) 
plusMinus([-4, 3, -9, 0, 4, 1])