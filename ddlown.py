class node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None
class doublelinked:
  def __init__(self):
    self.head=None
    self.first=None
    self.count=0

  def create(self):
    n=int(input("enter data: "))
    newnode=node(n)
    if self.head is None:
      self.head=self.first=newnode
    else:
      self.first.next=newnode
      newnode.prev=self.first
      self.first=newnode
    self.count+=1
  def display_forward(self):
    temp=self.head
    while temp:
      print(f"{temp.data}<->",end="")
      temp=temp.next
    print("NULL")
  def display_back(self):
    temp=self.first
    while temp:
      print(f"{temp.data}<->",end="")
      temp=temp.prev
    print("NULL")
def main():
  dll=doublelinked()
  while True:
     print("\n1. Create  2. Display Forward  3. Display Backward  4. Exit")
     ch = int(input("Enter choice: "))
     if ch == 1:
         dll.create()
     elif ch == 2:
        dll.display_forward()
     elif ch == 3:
        dll.display_back()
     elif ch == 4:
        print("Exiting...")
        break
     else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
    


