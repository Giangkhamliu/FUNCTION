## Write function here
# function_name(“hello”,”welcome”)
# function_name(“sonu”,”monu”)
def names_in_string(name1,name2):
    length1=len(name1)
    length2=len(name2)
    if length1>length2:
        print(name1)
    elif length1<length2:
        print(name2)
    else:
        print(name1)
        print(name2)
name1=input("Enter any string:-")
name2=input("Enter any string:-")
names_in_string(name1,name2)
