string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
def original(string_list):
    i=0
    while i<len(string_list):
        j=i+1
        while  j<len(string_list):
            if string_list[i]==string_list[j]:
                del string_list[i]
            j+=1
        i+=1
    print(string_list)
original(string_list)