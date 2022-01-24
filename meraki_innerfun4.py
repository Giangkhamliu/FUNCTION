# Define a function which takes one argument which is the limit upto which 
# the function has to print the numbers and their label(even or odd) as shown below.
def number(num):
    i=0
    while i<=num:
        if i%2==0:
            print(i,"Even")
        else:
            print(i,"Odd")
        i+=1
num=int(input("Enter the desired number:-"))
number(num)                                                                                                 