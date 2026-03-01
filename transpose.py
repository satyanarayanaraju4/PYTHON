row=int(input("enter row values: "))
cols=int(input("enter cols values: "))
matrix=[]
print("enter values row by row: ")
for i in range(row):
  rows=[]
  for j in range(cols):
    val=int(input())
    rows.append(val)
  print("enter new row values: ")
  matrix.append(rows)
print("the matrix values is: ")
for r in matrix:
  for j in r:
    print(j,end=" ")
  print()
print("transpose of matrix is : ")
transpose=[]
for j in range(cols):
  rows=[]
  for i in range(row):
    rows.append(matrix[i][j])
  transpose.append(rows)
for r in transpose:
  for j in r:
    print(j,end=" ")
  print()