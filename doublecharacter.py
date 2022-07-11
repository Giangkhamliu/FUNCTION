def double_letters(letters):
    i=0
    while i<len(letters)-1:
        if letters[i] == letters[i+1]:
            return True
        i=i+1
    return False
print(double_letters(letters=input("enter you chr: ")))




# The goal of this challenge is to analyze a string to check if it contains two of
#  the same letter in a row. For example, the string "hello" has l twice in a row,
#  while the string "nono" does not have two identical letters in a row.
# Define a function named double_letters that takes a single parameter. 
# The parameter is a string. Your function must return True if there are two
#  identical letters in a row in the string, and False otherwise.
def double_letters(string):
    i=0
    j=i+1
    b=[]
    while i<len(string) and j<len(string):
        if string[i]==string[j]:
            a=True
        else:
            a=False
        i+=1
        j+=1
        b.append(a)
    print(b)
    if True in b:
        return True
    else:
        return False
string=input("Enter the string:-")
print(double_letters(string))
