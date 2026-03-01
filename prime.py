def isprime(m):
  count=0
  for i in range(1,m + 1):
    if m%i==0:
      count+=1
  return count

a=int(input("enter a number: "))
factors=isprime(a)
if factors==2:
  print("prime number")
else:
  print("not prime number")
