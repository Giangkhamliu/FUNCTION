def sum_array(arr):
    sum=0
    if arr==None or len(arr)<=2:
        return 0
    else:
        a=min(arr)
        b=max(arr)
        i=0
        while i<len(arr):
            sum+=arr[i]
            i+=1
        c=sum-(a+b)
        return c
print(sum_array([3]))
print(sum_array(None))
print(sum_array([]))
print(sum_array([-3]))
print(sum_array([3,5]))
print(sum_array([-3,-5]))
print(sum_array([6,2,1,8,10]))
print(sum_array([6,0,1,10,10]))
print(sum_array([-6,20,-1,10,-12]))