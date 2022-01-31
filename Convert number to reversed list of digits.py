# Given a random number non-negative ,you have to return the digits of 
# this number within an array in reverse order
# Example:
# 348597=> [7,9,5,8,4,3]
# Problem statement:
# (i)digit=7567
# Output should be=>[7,6,5,7]
# (ii) digit=4523
# Output should=> [3,2,5,4]

def reverse(num):
    string=str(num)
    a=[]
    i=len(string)
    while i>0:
        c=string[i-1]
        a.append(int(c))
        i-=1
    print(a)
reverse(348597)
reverse(7567)
reverse(4523)
