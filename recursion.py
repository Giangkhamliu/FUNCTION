# from re import I
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i+=1
#     print("hello",i)
#     greet()
# greet()


# factorial using recursion
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result=fact(5)
# print(result)

# fibonnaci series
#  0 1 1 2 3 5 8 13 21
#  0 1 2 3 4 5 6  7  8 
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(6))