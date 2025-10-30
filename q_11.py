'''
Write a python program to demonstrate a circular linked list using SLL with following operations.
Insert an elements at the beginning.
Insert an elements at the end.
Add the given position in the list.
Delete elements from the beginning.
Delete elements from the end.
Delete the element from specific position.
'''

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Singly Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Utility: Display list
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    # 2. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # 3. Insert at given position (0-based index)
    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        count = 0
        while count < pos - 1 and temp.next != self.head:
            temp = temp.next
            count += 1
        if temp.next == self.head and count < pos - 1:
            print("Position out of range!")
            return
        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    # 5. Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    # 6. Delete from specific position
    def delete_from_position(self, pos):
        if self.head is None:
            print("List is empty!")
            return
        if pos == 0:
            self.delete_from_beginning()
            return
        temp = self.head
        count = 0
        while count < pos - 1 and temp.next != self.head:
            temp = temp.next
            count += 1
        if temp.next == self.head:
            print("Position out of range!")
            return
        temp.next = temp.next.next


# ------------------ Main Program ------------------
cll = CircularLinkedList()

while True:
    print("\n--- Circular Singly Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Display List")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        cll.insert_at_beginning(val)
    elif choice == 2:
        val = int(input("Enter value: "))
        cll.insert_at_end(val)
    elif choice == 3:
        val = int(input("Enter value: "))
        pos = int(input("Enter position (0-based index): "))
        cll.insert_at_position(val, pos)
    elif choice == 4:
        cll.delete_from_beginning()
    elif choice == 5:
        cll.delete_from_end()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        cll.delete_from_position(pos)
    elif choice == 7:
        cll.display()
    elif choice == 8:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.")
