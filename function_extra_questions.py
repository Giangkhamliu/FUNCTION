# Write a function called fizz_buzz that takes a number.
# 1. If the number is divisible by 3, it should return “Fizz”.
# 2. If it is divisible by 5, it should return “Buzz”.
# 3. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# 4. Otherwise, it should return the same number.
def fizz_buzz(num):
    if num%3==0:
        if num%5==0:
            if num%3==0 and num%5==0:
                return "FizzBuzz"
            else:
                return "Buzz"
        else:
            return "Fizz"
    else:
        return num
num=int(input("Enter any number:-"))
print(fizz_buzz(num))