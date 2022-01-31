#  list=[1 , 3 , 8 , 1 , 8]
# Sample output=12
# Sample input
# list=[-1,-1,5,2,-7]
# Sample output=-1
# Sample input
# list= Sample input
# list=[  ]
# Sample output=None
def unique_sum(list):
    i=0
    a=[]
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
            b=sum(a)
        i+=1
    print(b)    
unique_sum([1,3,8,1,8])
unique_sum([-1,-1,5,2,-7])
