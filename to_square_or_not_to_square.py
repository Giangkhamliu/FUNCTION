def square_or_square_root(arr):
    r=[]
    for i in arr:
        if i**0.5==int(i**0.5):
            r.append(int(i**0.5))
        else:
            r.append(i**2)
    return r
print(square_or_square_root([1,2,3,4,9,16]))