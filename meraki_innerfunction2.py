# Define a function named perfect() which takes one argument(integer) and checks if it
# is a perfect number or not. Now use this code to write a program that prints all the 
# perfect numbers between 1-1000.Define a function named perfect() which takes one 
# argument(integer) and checks if it is a perfect number or not.Now use this code
#  to write a program that prints all the perfect numbers between 1-1000.
def perfect(number):    
    for num in range(1,number+1):
        sum=0
        for i in range(1,num):
            if num%i==0:
               sum=sum+i
        if sum==num:
            print(num,end=" ")
number=int(input("Enter the number:-"))
perfect(number)

