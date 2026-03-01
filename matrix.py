rows=int(input("Enter the no of rows: "))
cols=int(input("enter the no of columns: "))
matrix=[]
print("enter the matrix values row by row: ")
for i in range(rows):
  row=[]
  for j in range(cols):
    val=int(input())
    row.append(val)
  print("enter new row values: ")
  matrix.append(row)
print("matrix values are: ")
for r in matrix:
  for j in r:
    print(j,end=" ")
  print()