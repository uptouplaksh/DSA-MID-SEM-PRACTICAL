'''
Write a python program to demonstrate a singly linked list with following operations.
Create List
Display elements of the list.
Search given element from list.
Count the number of nodes in the list.
'''

# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 3. Insert at specific position
    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for i in range(pos - 1):
            if temp is None:
                print("Position out of range.")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range.")
        else:
            new_node.next = temp.next
            temp.next = new_node

    # 4. Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty!")
            return
        self.head = self.head.next

    # 5. Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # 6. Delete from specific position
    def delete_from_position(self, pos):
        if self.head is None:
            print("List is empty!")
            return
        if pos == 0:
            self.delete_from_beginning()
            return
        temp = self.head
        for i in range(pos - 1):
            if temp is None or temp.next is None:
                print("Position out of range.")
                return
            temp = temp.next
        temp.next = temp.next.next

    # 7. Delete by given value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print("Value not found.")
        else:
            temp.next = temp.next.next

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# ------------------ Main Program ------------------
linked_list = SinglyLinkedList()

while True:
    print("\n--- Singly Linked List Operations ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Delete by Value")
    print("8. Display List")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        linked_list.insert_at_beginning(data)
    elif choice == 2:
        data = int(input("Enter value: "))
        linked_list.insert_at_end(data)
    elif choice == 3:
        data = int(input("Enter value: "))
        pos = int(input("Enter position (0-based index): "))
        linked_list.insert_at_position(data, pos)
    elif choice == 4:
        linked_list.delete_from_beginning()
    elif choice == 5:
        linked_list.delete_from_end()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        linked_list.delete_from_position(pos)
    elif choice == 7:
        value = int(input("Enter value to delete: "))
        linked_list.delete_by_value(value)
    elif choice == 8:
        linked_list.display()
    elif choice == 9:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")
