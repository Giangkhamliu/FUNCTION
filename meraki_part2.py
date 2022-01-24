list_change=([5, 10, 50, 20], [2, 20, 3, 5])
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

    