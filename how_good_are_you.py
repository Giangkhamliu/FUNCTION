def better_than_average(class_points, your_points):
    sum=0
    avg=0
    i=0
    while i<len(class_points):
        sum+=class_points[i]
        i+=1
    sum=sum+your_points
    avg=sum/int(len(class_points)+1)
    if avg<your_points:
        return True
    else:
        return False
print(better_than_average([3,2],5))
print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21))