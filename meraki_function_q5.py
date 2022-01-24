# def calculator(number_x,number_y,operator):
#     if operator=="add":
#         sum=number_x+number_y
#         print(sum)
#     elif operator=="subtract":
#         minus=number_x-number_y
#         print(minus)
#     elif operator=="multiply":
#         mul=number_x*number_y
#         print(mul)
#     elif operator=="divide":
#         div=number_x/number_y
#         print(div)
#     elif operator=="modulus":
#         mod=number_x%number_y
#         print(mod)
# number_x=int(input("Enter the first numbers:-"))
# number_y=int(input("Enter the second numbers:-"))
# operator=input("Enter the desired operators:-")
# calculator(number_x,number_y,operator)


#PART2

# list_change=([5, 10, 50, 20], [2, 20, 3, 5])
def list_change(num1,num2):
    new_list=[]
    i=0
    j=0
    while i<len(num1) and j<len(num2):
        multiply=num1[i]*num2[j]
        new_list.append(multiply)
        i+=1
        j+=1
    print(new_list)
list_change([5,10,50,20],[2,20,3,5])

    