'''
Write a python program to demonstrate a doubly linked list with following operations.
Create List
Display elements of the list.
Search given element from list.
Count the number of nodes in the list.
'''

# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create List
    def create_list(self, elements):
        for data in elements:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
                new_node.prev = temp

    # 2. Display elements of the list
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        print("Doubly Linked List elements:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # 3. Search a given element from list
    def search(self, key):
        temp = self.head
        position = 1
        while temp:
            if temp.data == key:
                print(f"Element {key} found at position {position}.")
                return
            temp = temp.next
            position += 1
        print(f"Element {key} not found in the list.")

    # 4. Count number of nodes in the list
    def count_nodes(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print(f"Total number of nodes: {count}")


# ------------------ Main Program ------------------
dll = DoublyLinkedList()

# Create list
n = int(input("Enter number of elements: "))
elements = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    elements.append(val)

dll.create_list(elements)

# Display list
dll.display()

# Search element
key = int(input("Enter element to search: "))
dll.search(key)

# Count nodes
dll.count_nodes()

