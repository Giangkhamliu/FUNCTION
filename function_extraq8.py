# Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])                      
list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
def max_min(list):
    i=0
    j=i+1
    new_list=[]
    while i<len(list) and j<len(list):      
        i+=1
    print(new_list)
max_min(list)