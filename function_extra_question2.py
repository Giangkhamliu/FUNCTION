#Write a function that prints all the prime numbers between 0 and limit
# where limit is a parameter.
def prime(n):
    print("Prime numbers are:-")
    i=0
    while i<=n:
        j=1
        count=0
        while j<=n:
            if i%j==0:
                count=count+1
            j=j+1
        if count==2:
            print(i,end=" ")        
        i=i+1
n=int(input("Enter the number:"))
prime(n)




