row1=int(input("enter matrix 1 row values: "))
cols1=int(input("enter matrix 1 cols values: "))
row2=int(input("enter matrix 2 row values: "))
cols2=int(input("enter matrix 2 cols values: "))
matrix1=[]
matrix2=[]
print("enter matrix1 values row by row: ")
for i in range(row1):
  rows=[]
  for j in range(cols1):
    val=int(input())
    rows.append(val)
  print("enter new row values: ")
  matrix1.append(rows)
print("enter matrix2 values row by row: ")
for i in range(row2):
  rows=[]
  for j in range(cols2):
    val=int(input())
    rows.append(val)
  print("enter new row values: ")
  matrix2.append(rows)
print("the matrix1 values is: ")
for r in matrix1:
  for j in r:
    print(j,end=" ")
  print()
print("the matrix2 values is: ")
for r in matrix2:
  for j in r:
    print(j,end=" ")
  print()
print("multiplication of matrix1 and matrix2 is: ")
addmat=[]
if(cols1==row1):
  for i in range(row1):
    add=[]
    for j in range(cols1):
      add.append(matrix1[i][j]*matrix2[i][j])
    addmat.append(add)
  for r in addmat:
    for j in r:
      print(j,end=" ")
    print()
else:
    print("multiplication is not possible!")