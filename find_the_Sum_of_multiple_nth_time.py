# Find the sum of all multiples of n below m
def mul(n,m):
    if n>0:
        sum=0
        i=1
        while n*i<m:
           multiply= n*i
           sum=sum+multiply
           i+=1
        return(sum)
    else:
        return ("INVALID")
print(mul(2,9))
print(mul(3, 13))  #==> 3 + 6 + 9 + 12 = 30
print(mul(4, 123)) #==> 4 + 8 + 12 + ... = 1860
print(mul(4, -7))