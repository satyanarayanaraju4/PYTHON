t=int(input())
arr=[]
for i in range(t):
  num=int(input())
  arr.append(num)
print("array before sorting")
print(*arr)
for i in range(t-1):
  is_swap=False
  for j in range(t-i-1):
    if arr[j]>arr[j+1]:
      arr[j],arr[j+1]=arr[j+1],arr[j]
      is_swap=True
  if not is_swap:
    break
print("array after sorting")
print(*arr)