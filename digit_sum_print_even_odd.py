def digit_sum(n):
    sum=0
    while n>0 or sum>9:
        if n==0:
            n=sum
            sum=0
        sum=sum+n%10
        n=n//10
    print("The sum is:-",sum)
    if sum%2==0:
        print("Even")
    else:
        print("Odd")
digit_sum(7654)