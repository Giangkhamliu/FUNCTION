def sum(sum_mix):
    sum=0
    i=0
    while i<len(sum_mix):
        sum+=int(sum_mix[i])
        i=i+1
    return sum
print(sum(['5','0',9,3,2,1,'9',6,7]))
print(sum(["3",6,6,0,'5',8,5,'6',2,'0'])) 
print(sum([1,3,6,9,'4',8,'3']))

