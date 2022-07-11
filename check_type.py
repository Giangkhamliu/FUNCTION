def only_ints(a,b):
    if type(a)==int and type(b)==int:
        return True
    else:
        return False
print(only_ints(3,4))
print(only_ints("a",4))