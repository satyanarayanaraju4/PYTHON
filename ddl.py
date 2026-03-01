class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.first = None  
        self.count = 0

    def create(self):
        d = int(input("Enter data: "))
        newnode = Node(d)
        if self.head is None:
            self.head = self.first = newnode
        else:
            self.first.next = newnode
            newnode.prev = self.first
            self.first = newnode
        self.count += 1

    def display_forward(self):
        temp = self.head
        while temp:
            print(f"{temp.data}<->", end="")
            temp = temp.next
        print("NULL")

    def display_back(self):
        temp = self.first
        while temp:
            print(f"{temp.data}<->", end="")
            temp = temp.prev
        print("NULL")

    def insert(self):
        pos = int(input(f"Enter position to insert (1-{self.count + 1}): "))
        x = int(input("Enter data: "))
        newnode = Node(x)

        if pos < 1 or pos > self.count + 1:
            print("Invalid position!")
            return

        if pos == 1:
            newnode.next = self.head
            if self.head:
                self.head.prev = newnode
            self.head = newnode
            if self.first is None:
                self.first = newnode
        else:
            temp = self.head
            for _ in range(1, pos - 1):
                temp = temp.next
            newnode.next = temp.next
            newnode.prev = temp
            if temp.next:
                temp.next.prev = newnode
            temp.next = newnode
            if pos == self.count + 1:
                self.first = newnode
        self.count += 1

    def delete(self):
        if self.first is None:
            print("List is empty!")
            return

        pos = int(input(f"Enter position to delete (1-{self.count}): "))

        if pos < 1 or pos > self.count:
            print("Invalid position!")
            return

        temp = self.head
        if pos == 1:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.first = None
        else:
            for _ in range(1, pos):
                temp = temp.next
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            else:
                self.first = temp.prev
        self.count -= 1

def main():
    dll = DoublyLinkedList()

    while True:
        print("\n1. Create  2. Display Forward  3. Display Backward  4. Insert  5. Delete  6. Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            dll.create()
        elif ch == 2:
            dll.display_forward()
        elif ch == 3:
            dll.display_back()
        elif ch == 4:
            dll.insert()
        elif ch == 5:
            dll.delete()
        elif ch == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()