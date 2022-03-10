# n=123
# k=3
# p=123123123=18
# output=9
# def digit_sum(n):
#     k=int(input("Enter the number of times to be multiply:-"))
#     p1=n*k
#     p=int(p1)
#     sum=0
#     while p>0 or sum>9:
#         if p==0:
#             p=sum
#             sum=0
#         sum=sum+p%10
#         p=p//10
#     print(sum)
# n=input("Enter the number:-")
# digit_sum(n)

def digit_sum(n):
    sum=0
    while n>0  or sum>9:
        if n==0:
           n=sum
           sum=0
        sum=sum+n%10
        n=n//10
    print(sum)
    if sum%2==0:
        print(True)
    else:
        print(False)
n=int(input("Enter the number:-"))
digit_sum(n)