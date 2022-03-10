# Write a Python function that takes a list and returns a new list with 
# que elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def list(lists):
    i=0
    while i<len(lists):
        j=i+1
        while j<len(lists):
            if lists[i]==lists[j]:
               del lists[j]
               continue
            j+=1
        i+=1
    print(lists)
list([1,2,3,3,3,3,4,5])