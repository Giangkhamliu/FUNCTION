numbers = [1, 2, 3, 4, 5]
def sum(numbers):
    i=0
    add=0
    while i<len(numbers):
        add+=numbers[i]
        i+=1
    print(add)
sum(numbers)