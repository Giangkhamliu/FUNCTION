def average(get_average):
    i=0
    sum=0 
    avg=0
    while i<len(get_average):
        sum=sum+get_average[i]
        i+=1
    avg=int(sum/len(get_average))
    return (avg)      
print(average([2, 2, 2, 2]))
print(average([1, 5, 87, 45, 8, 8]))
print(average([2,5,13,20,16,16,10]))
print(average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]))
    
