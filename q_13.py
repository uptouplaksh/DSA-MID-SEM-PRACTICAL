'''
Write a python program to demonstrate a doubly linked list with following operations.
Insert an elements at the beginning.
Insert an elements at the end.
Add the given position in the list.
Delete elements from the beginning.
Delete elements from the end.
Delete the element from specific position.
Delete the element by given value
'''

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        print("Doubly Linked List:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(f"Inserted {data} at the beginning.")

    # 2. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"Inserted {data} at the end.")

    # 3. Insert at given position
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position <= 1 or self.head is None:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(position - 2):
            if temp.next is None:
                break
            temp = temp.next
        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp
        print(f"Inserted {data} at position {position}.")

    # 4. Delete element from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        print(f"Deleted {self.head.data} from beginning.")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # 5. Delete element from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        temp = self.head
        if temp.next is None:
            print(f"Deleted {temp.data} from end.")
            self.head = None
            return
        while temp.next:
            temp = temp.next
        print(f"Deleted {temp.data} from end.")
        temp.prev.next = None

    # 6. Delete element from specific position
    def delete_from_position(self, position):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if position <= 1:
            self.delete_from_beginning()
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range.")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range.")
            return
        print(f"Deleted {temp.data} from position {position}.")
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    # 7. Delete element by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                print(f"Deleted element {value}.")
                return
            temp = temp.next
        print(f"Element {value} not found in list.")


# ---------------- MAIN PROGRAM ----------------
dll = DoublyLinkedList()

while True:
    print("\n--- Doubly Linked List Operations ---")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at specific position")
    print("4. Delete from beginning")
    print("5. Delete from end")
    print("6. Delete from specific position")
    print("7. Delete by value")
    print("8. Display list")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        dll.insert_at_beginning(val)
    elif choice == 2:
        val = int(input("Enter value: "))
        dll.insert_at_end(val)
    elif choice == 3:
        val = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        dll.insert_at_position(val, pos)
    elif choice == 4:
        dll.delete_from_beginning()
    elif choice == 5:
        dll.delete_from_end()
    elif choice == 6:
        pos = int(input("Enter position: "))
        dll.delete_from_position(pos)
    elif choice == 7:
        val = int(input("Enter value to delete: "))
        dll.delete_by_value(val)
    elif choice == 8:
        dll.display()
    elif choice == 9:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
