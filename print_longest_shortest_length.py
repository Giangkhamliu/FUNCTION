#  Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])


def max_length_list(list1):
    max_length = max(len(x) for x in list1 )
    max_list = max(list1, key = len)
    return(max_length, max_list)
def min_length_list(list1):
    min_length = min(len(x) for x in list1 )
    min_list = min(list1, key = len)
    return(min_length, min_list)
list1=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("List with maximum length of lists:")
print(max_length_list(list1))
print("List with minimum length of lists:")
print(min_length_list(list1))
