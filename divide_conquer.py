# Given a mixed array of number and string 
# representations of integers, add up the string integers
# and subtract this from the total of the non-string integers.

def div_con(x):
    
    s=0
    d=0
    i=0
    while i<len(x):
        if type(x[i])==str:
            s+=int(x[i])
        else:
            d+=x[i]
        i+=1
    return d-s
    
print(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))
print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))
print(div_con(['1', '5', '8', 8, 9, 9, 2, '3']))