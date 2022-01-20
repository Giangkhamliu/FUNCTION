# def solution(s):
#     return s[::-1]

def solution(s):
    str1=''
    i=len(s)
    while i>0:
        str1+=s[i-1]
        i-=1
    print(str1)
solution("grace")