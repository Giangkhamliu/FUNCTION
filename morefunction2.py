list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
def unique(list1,list2):
    i=0
    while i<len(list1):
        j=0
        while j<len(list2):
            if list1[i]==list2[j]:
                del list1[i]
            j+=1
        i+=1
    new_list=list1+list2
    new_list.sort()
    print(new_list)
unique(list1,list2)