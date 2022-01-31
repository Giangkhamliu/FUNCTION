# Sample input
# list1=["tail", "body", "head"]
# Output
# => ["head", "body", "tail"]
# Sample input
# list=["bottom", "middle", "top"]
# output
# ["top", "middle", "bottom"]
# Sample input
# list=["lower legs", "torso", "upper legs"]
# Output
# ["upper legs", "torso", "lower legs"]
def ordered(list):
    a=[]
    i=-1
    while i>=-(len(list)):
        a1=list[i]
        a.append(a1)
        i-=1
    print(a)
ordered(["tail", "body", "head"])
ordered(["bottom", "middle", "top"])
ordered(["lower legs", "torso", "upper legs"])