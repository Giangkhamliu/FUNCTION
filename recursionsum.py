def recur(num):
   n=str(num)
   i=0
   sum=0
   while i<len(n):
      sum=sum+int(n[i])
      i+=1
   si=str(sum)
   if len(si)==1:
      print(si)
   else:
      n=si
      return(recur(sum))
      
num=int(input("enter the number:"))
recur(num)