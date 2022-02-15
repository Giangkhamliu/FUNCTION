# Q9.Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
def square(num):
    a=[]
    i=1
    while i<=num:
        a.append(i*i)
        i+=1
    j=1
    b=[]
    while j<len(a):
        c=a[0:5:1]
        d=a[-5::]
        j+=1
    b.append(c)
    b.append(d)
    print(b)
    
# num=int(input("Enter the num:-"))
square(30)