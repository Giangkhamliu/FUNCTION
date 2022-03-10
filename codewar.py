# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r",
#  you are playing banjo!

def are_you_playing_banjo(name):
    name1=list(name)
    i=0
    while i<len(name1):
       if name1[0]=="R" or name1[0]=="r":
           return name
print(are_you_playing_banjo("race"))

# name="Grace"
# print(len(name))
# if name[0]=="r" or name[0]=="R":
#     print("Yes")
# else:
#     print("nNO")

# def count_sheeps(sheep):
#     count=0
#     i=0
#     while i<len(sheep):
#         if sheep[i]==True:
#             count=count+1
#         i+=1
#     return count
# print(count_sheeps([True,True,False,True,False,True,True,False,True,True,True,False,True]))

# ROCK PAPER SCISSOR:
# def rps(p1, p2):
#     if((p1=="scissors")and(p2=="paper"))or((p1=="paper") and (p2=="rocks")) or ((p1=="rock") and (p2=="scissors")) :
#         return("Player 1 won !")
#     elif(p2=="scissors" and p1=="paper") or (p2=="paper" and p1=="rocks") or (p2=="rock" and p1=="scissors"):
#         return("Player 2 won !")
#     elif (p1==p2):
#         return("Draw!")
# print(rps("rocks","paper"))
# 
# write me a function stringy that takes a size and returns a string of
#  alternating '1s' and '0s'.the string should start with a 1.
# a string with size 6 should return :'101010'.
# def stringy(size):
#     i=1
#     while i<=size:
#         if i%2==0:
#             print("0",end="")
#         else:
#             print("1",end="")
#         i+=1 
# stringy(6)

def correct_tail(body, tail):
    sub=body[-1]
    if sub==tail:
           return True
    else:
           return False
print(correct_tail("Fox","x"))