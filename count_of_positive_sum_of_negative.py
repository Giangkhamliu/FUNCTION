def numbers(list):
    i=0
    count=0
    sum=0
    b=[]
    while i<len(list):
        if list[i]>0:
            count+=1
        elif list[i]<0:
            sum=sum+list[i]
        i+=1
    if count==0 and sum==0:
        b=[]
    else:
        b.append(count)
        b.append(sum)
    return b
    
print(numbers([1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]))
print(numbers([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(numbers([1]))
print(numbers([-1]))
print(numbers([0,0,0,0,0,0,0,0]))
print(numbers([]))



