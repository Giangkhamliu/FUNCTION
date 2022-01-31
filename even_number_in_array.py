def evn_no(array):
    length=0
    a=[]
    i=0
    while i<len(array):
        if array[i]%2==0:
            if array[i] not in a:
                a.append(array[i])
                a.sort()
                length+=1
        i+=1
    print(a)
    print(length)
evn_no([1,2,3,4,5,6,7,8,9])
evn_no([-22,5,3,11,26,-6,-7,-8,-9,-8,26])
evn_no([6,-25,3,7,5,5,7,-3,23])
