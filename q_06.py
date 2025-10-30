'''
Write a python program to:
Add elements at the beginning.
Add elements at the end.
Add the given position in the list.
Delete elements at the beginning.
Delete elements at the end.
Reverse a list.
'''

# Create a list
lst = [10, 20, 30, 40, 50]
print("Original List:", lst)

# 1. Add element at the beginning
val = int(input("Enter element to add at beginning: "))
lst.insert(0, val)
print("After Adding at Beginning:", lst)

# 2. Add element at the end
val = int(input("Enter element to add at end: "))
lst.append(val)
print("After Adding at End:", lst)

# 3. Add element at a given position
pos = int(input("Enter position to insert at (0-based index): "))
val = int(input("Enter element to add: "))
if 0 <= pos <= len(lst):
    lst.insert(pos, val)
    print("After Adding at Position", pos, ":", lst)
else:
    print("Invalid position!")

# 4. Delete element at the beginning
if len(lst) > 0:
    lst.pop(0)
    print("After Deleting from Beginning:", lst)
else:
    print("List is empty, cannot delete!")

# 5. Delete element at the end
if len(lst) > 0:
    lst.pop()
    print("After Deleting from End:", lst)
else:
    print("List is empty, cannot delete!")

# 6. Reverse the list
lst.reverse()
print("Reversed List:", lst)
