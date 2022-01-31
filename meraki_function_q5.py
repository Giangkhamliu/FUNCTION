def calculator(number_x,number_y,operator):
    if operator=="add":
        sum=number_x+number_y
        print(sum)
    elif operator=="subtract":
        minus=number_x-number_y
        print(minus)
    elif operator=="multiply":
        mul=number_x*number_y
        print(mul)
    elif operator=="divide":
        div=number_x/number_y
        print(div)
    elif operator=="modulus":
        mod=number_x%number_y
        print(mod)
number_x=int(input("Enter the first numbers:-"))
number_y=int(input("Enter the second numbers:-"))
operator=input("Enter the desired operators:-")
calculator(number_x,number_y,operator)




