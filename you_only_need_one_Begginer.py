# Challenge name:- You only need one-Beginner
# Problem statement:-
# array=[66, 101]
# value=66
# output=true
# array=[78, 117, 110, 99, 104, 117, 107, 115]
#           value=8
#           output=false
# array=['t', 'e', 's', 't']
#           value='e'
#           output=true
# array=["what", "a", "great", "kata"]
# value='kat'
# output=false
def check(a):
    check_num=(input("Enter the no.:-"))
    if check_num in a:
        print("True")
    else:
        print("False")
check([66,101])
check([78, 117, 110, 99, 104, 117, 107, 115])
check(['t', 'e', 's', 't'])
check(["what", "a", "great", "kata"])