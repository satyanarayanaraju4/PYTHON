# Simple switch program using match-case in Python 3.10+
while True:
 print("Menu:")
 print("1. Say Hello \n2. Say Goodbye \n3. Exit")


 choice = int(input("Enter your choice: "))

 match choice:
    case 1:
        print("Hello!")
    case 2:
        print("Goodbye!")
    case 3:
        print("Exiting program...")
    case default:
        print("Invalid choice.")

