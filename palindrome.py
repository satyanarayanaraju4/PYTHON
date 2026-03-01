a=int(input("enter a number: "))
sum=0
num=a
while a>0:
  digit=a%10
  sum=sum*10+digit
  a=a//10
if sum==num:
  print("palindrome")
else:
  print("not palindrome")