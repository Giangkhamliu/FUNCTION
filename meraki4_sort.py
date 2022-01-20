# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# def sorting(unorder_list):
#     unorder_list.sort()
#     print(unorder_list)
# sorting(unorder_list)

# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# def sorting(unorder_list):
#     unorder_list.sort()
#     return unorder_list
# print(sorting(unorder_list))

# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# def sorting(unorder_list):
#     i=0
#     a=0
#     while i<len(unorder_list):
#         j=0
#         while j<len(unorder_list):
#             if unorder_list[i]<unorder_list[j]:
#                 a=unorder_list[j]
#                 unorder_list[j]=unorder_list[i]
#                 unorder_list[i]=a
#             j+=1                               
#         i+=1
#     return unorder_list
# print(sorting(unorder_list))                                                                            
                                                                     

unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
def sorting(unorder_list):
    i=0
    a=0
    while i<len(unorder_list):
        j=0
        while j<len(unorder_list):
            if unorder_list[i]<unorder_list[j]:
                a=unorder_list[j]
                unorder_list[j]=unorder_list[i]
                unorder_list[i]=a
            j+=1
        i+=1
    print(unorder_list)
sorting(unorder_list)                                                                          
                                                                     