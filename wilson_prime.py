def am_i_wilson(n):
    #     the only known wilson prime are 5,13,563
    if n in (5,13,563):
        return True
    else:
        return False
print(am_i_wilson(9))
print(am_i_wilson(3))
print(am_i_wilson(1))
print(am_i_wilson(5))