# Create a function called shortcut to remove all the lowercase vowels in a given string.
# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# def lowercase():
#     lowercase=input("Enter the string:-")
#     vowel='aeiou'
    
#     i=0
#     while i<len(lowercase):
#         j=0
#         while j<len(vowel):
#             if lowercase[i] in vowel:
#                 del lowercase[i]
#             i+=1
#         j+=1
#     print(lowercase)
# lowercase()
lowercase=input("Enter the string:-")
a=''
vowel='aeiou'
print(len(lowercase))
print(len(vowel))
i=0
while i<len(lowercase):
    j=0
    while j<len(vowel):
       if lowercase[i] in vowel[j]:
           print(a.remove(lowercase[i]))
       j+=1
    
    i+=1
