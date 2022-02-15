# num= ["Z","A","A","B","E","M","A","R","D"]
# def reverse_list(num):
#     num.reverse()
#     return num
# print(reverse_list(num))

num= ["Z","A","A","B","E","M","A","R","D"]
def reverse_list(num):
    i=-1
    a=[]
    while i>-(len(num)+1):
        a.append(num[i])
        i-=1
    print(a)
reverse_list(num)



