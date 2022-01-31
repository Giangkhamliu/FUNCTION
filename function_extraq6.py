# [10, 14, 2, 23, 19] --> 42 (= 23 + 19)
# [99, 2, 2, 23, 19] --> 122 (= 99 + 23)
def list(list1):
    list1.sort()
    i=0
    while i<len(list1):
        a=list1[-1]+list1[-2]
        i+=1
    print(a)
list([10, 14, 2, 23, 19])
list([99, 2, 2, 23, 19])
