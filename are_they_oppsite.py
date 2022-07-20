def is_opposite(s1,s2):
    s3=s1.swapcase()
    if s3==s2 and s3!="":
        return True
    else:
        return False
print(is_opposite("",""))
print(is_opposite("AB","Ab"))
print(is_opposite("aBcd","AbCD"))
print(is_opposite("ab","AB"))