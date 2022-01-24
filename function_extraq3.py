# Your goal is to return multiplication table for number that is always an integer from 1 to
# 10.For example, a multiplication table (string) for number == 5 looks like below:- 
# 1 * 5 =5
# 2 * 5 =10
# 3 * 5 =15
# .
# .
# 10 * 5=50
def multiplication(number):
    i=1
    while i<=10:
        print(i,"*",number,"=",i*number)
        i+=1
number=int(input("Enter any number:-"))
multiplication(number)