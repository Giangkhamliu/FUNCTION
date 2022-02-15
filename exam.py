founder=1
def ask_question():
   print("who is the founder of facebook?")
   print("1.Mark Zuckerberg \n2.Bill gates \n3.Larry page \n4.steve Job")
   ans=int(input("Enter your answer: "))
   if ans==founder:
      print("true")
   else:
      print("wrong answer")
ask_question()