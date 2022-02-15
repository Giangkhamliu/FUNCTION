def string(s):
    c_upper=0
    c_lower=0
    i=0
    while i<len(s):
        if (s[i]>"A" and s[i]<"Z"):
            c_upper+=1
        elif (s[i]>"a" and s[i]<"z"):
            c_lower+=1
        else:
            pass
        i+=1
    print("Uppercase:-",c_upper)
    print("Lower:-",c_lower)
s=input("Enter the string:")
string(s)

##OR

# def string(s):
#     c_upper=0
#     c_lower=0
#     i=0
#     while i<len(s):
#         if (s[i]>"A" and s[i]<"Z"):
#             c_upper+=1
#         elif s[i]>"a" and s[i]<"z":
#             c_lower+=1
#         else:
#             pass
#         i+=1
#     print("Uppercase:-",c_upper)
#     print("Lower:-",c_lower)
# string("The quick Brown Fox")



