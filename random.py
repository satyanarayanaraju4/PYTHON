
import math
def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
      return False
  return True

a=int(input("enter 1st number:  "))
b=int(input("enter 2nd number:  "))
for i in range(a,b+1):
  if(is_prime(i)):
    print(i)
