def well(x):
    i=0
    count_good=0
    count_bad=0
    while i<len(x):
        if x[i]=='good':
            count_good+=1
        else:
            count_bad+=1
        i+=1
    if count_good==1 or count_good==2:
        return "Publish!"
    elif count_good>2:
        return "I smell a series!"
    else:
        return "Fail!"
print(well(["bad","bad","bad","bad","bad"]))
print(well(["bad","bad","bad","bad","bad","good","good","good"]))
print(well(["good","good","good","good","good"]))
print(well(["bad","bad","good","good"]))