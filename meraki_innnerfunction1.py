# Create a funciton named eligibleforvote which tell the user if he/she is eligible
#  to vote or not.( Consider minimum age of voting to be 18. )
def eligible_for_vote(age):
    if age>=18:
        print("Eligible")
    else:
        print("Not Eligible")
age=int(input("Enter the age:-"))
eligible_for_vote(age)
