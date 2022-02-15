# def sequence(unique_in_order):
#     i=0
#     j=i+1
#     a=[]
#     while i<len(unique_in_order)and j<len(unique_in_order):
#         if unique_in_order[i]==unique_in_order[j]:
#             del unique_in_order[i]
#             a.append(unique_in_order)
#         i+=1
#         j+=1
#     print(unique_in_order)
# sequence([1,2,2,3,3])

def sequence(unique_in_order):
    i=0
    j=i+1
    a=[]
    while i<len(unique_in_order)and j<len(unique_in_order):
        if unique_in_order[i]!=unique_in_order[j]:
            b=unique_in_order[-1]
            a.append(unique_in_order[i])
        i+=1
        j+=1
    print(a+list(b))
sequence('AAAABBBCCDAABBB')
sequence('ABBCcAD')