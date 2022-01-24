#Create a function which takes 3 arguments(all integers) and prints
# their sum and average as shown below.
def sum_and_average(num1,num2,num3):
    sum=num1+num2+num3
    print(sum)
    avg=sum/3
    print(int(avg))
num1=int(input("Enter the first number:-"))
num2=int(input("Enter the second number:-"))
num3=int(input("Enter the third number:-"))
sum_and_average(num1,num2,num3)