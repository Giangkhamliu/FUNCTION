def count_positives_sum_negatives(arr):
    pos=0
    sum=0
    a=[]
    i=0
    if arr!=[]:
        while i<len(arr):
            if arr[i]<0:
                sum+=arr[i]
            elif arr[i]>0:
                pos=pos+1
            i+=1
            a.append(pos)
            a.append(sum)
        print(a) 
    else:
        print([])
count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])