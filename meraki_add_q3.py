# Write add_numbers function here
# num1 = 56
# num2 = 12
# def add_numbers(num1,num2):
#     print(num1+num2)
# add_numbers(56,12)

#PART 2
list1=[50, 60, 10]
list2=[10, 20, 13]
def add_two_lists(list1,list2):
    i=0
    j=0
    while i<len(list1) and j<len(list2):
        list=list1[i]+list2[j]
        print(list)
        i+=1
        j+=1
add_two_lists(list1,list2)
    
