'''
Write a python program to demonstrate a circular linked list using SLL with following operations.
Create List
Display elements of the list.
'''

# Node class to represent each element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Singly Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create list
    def create_list(self, elements):
        for data in elements:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                new_node.next = self.head  # point to itself
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = new_node
                new_node.next = self.head

    # 2. Display elements of the list
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        print("Circular Linked List elements:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


# ------------------ Main Program ------------------
cll = CircularLinkedList()

# Create list
n = int(input("Enter number of elements: "))
elements = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    elements.append(val)

cll.create_list(elements)

# Display list
cll.display()
