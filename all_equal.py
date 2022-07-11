# All equal
# Define a function named all_equal that takes a list and checks whether all
# elements in the list are the same.
# For example, calling all_equal([1, 1, 1]) should return True.
# Eg:[] return True
# [1] return True
# [1,1,1,1,1] return True
def all_equal(num):
    if len(num)==1 or len(num)==0:
        return True
    else:
        i=0
        j=i+1
        while i<len(num) and j<len(num):
            if num[i]==num[j]:
                return True
            else:
                return False
            
print(all_equal([1,1,1,1,1]))
print(all_equal([1,2,3,4,1]))
print(all_equal([]))
print(all_equal([1]))
print(all_equal([1,1,1,1]))
