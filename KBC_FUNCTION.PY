def kbc():
    print("🥰WELCOME TO KBC🥰")
    print("Here are the questions:")
    question= ["How many continents are there?","What is the capital of India?",
    "What course is offered in NG?"]
    options=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
    solution=[3,4,1]
    life5050=[["Nine", "Seven"],["Chennai", "Delhi"],["Software Engineering","Agriculturen"]]
    lifeans=[2,2,1]
    i=0
    j=0
    count=0
    while i<len(question)and j<len(options):
        print(j+1,question[i])
        k=0
        while k<(len(options)+1):
            print(k+1,options[j][k])
            k+=1
        life=input("Do you want 5050 life?Enter y or n:")
        if life=="y":
            if count==0:
                l=0
                while l<len(life5050[i]):
                    print(l+1,life5050[i][l])
                    l+=1
                count+=1
                sol1=int(input("Enter your solution:"))
                if sol1==lifeans[i]:
                    print("Congrats! your answer is correct.")
                else:
                    print("Sorry! 🥺Your answer is incorrect.")
                    break
            else:
                print("Your lifeline has been used. ")
                sol=int(input("Enter the solution:"))
                if sol==solution[i]:
                    print("Congratulation!!👍 Your Answer is correct.")
                else:
                    print("🥺Better luck next time.")
                    break
        elif life=="n":    
            sol=int(input("Enter the solution:"))
            if sol==solution[i]:
                print("Congratulation!! 👍Your Answer is correct.")
            else:
                print("🥺Better luck next time.")
                break
        print()
        i=i+1
        j+=1
kbc()