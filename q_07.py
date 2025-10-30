'''
Write a python program to perform various string manipulations using an array
Reversing a String.
String Slicing
Counting Occurrences of Each Character
Accessing characters in Python String
Deleting a Specific Character from a string
'''

# Python program to perform various string manipulations

# Input string
string = input("Enter a string: ")
print("\nOriginal String:", string)

# 1. Reversing a String
reversed_string = string[::-1]
print("\n1️⃣ Reversed String:", reversed_string)

# 2. String Slicing
start = int(input("\nEnter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
sliced = string[start:end]
print(f"Sliced String ({start}:{end}):", sliced)

# 3. Counting Occurrences of Each Character
print("\n3️⃣ Occurrences of Each Character:")
for char in set(string):  # using set to avoid duplicates
    print(f"'{char}' → {string.count(char)} time(s)")

# 4. Accessing characters in Python String
index = int(input("\nEnter index to access character: "))
if 0 <= index < len(string):
    print(f"Character at index {index} is '{string[index]}'")
else:
    print("Invalid index!")

# 5. Deleting a Specific Character from a String
ch = input("\nEnter character to delete: ")
new_string = string.replace(ch, "")
print(f"After deleting '{ch}':", new_string)
