"""
Write a program to create an array of 10 elements and
Print array
Count Occurrences of given Element
Find the max element from the array
Find min element from array
Find the sum and average of an array of elements
"""

# Create an array of 10 elements
arr = [12, 45, 23, 12, 67, 45, 89, 12, 34, 56]

# i. Print array
print("Array elements:", arr)

# ii. Count occurrences of a given element
element = int(input("Enter element to count: "))
count = arr.count(element)
print(f"Occurrences of {element}: {count}")

# iii. Find the max element
max_element = max(arr)
print("Maximum element:", max_element)

# iv. Find the min element
min_element = min(arr)
print("Minimum element:", min_element)

# v. Find the sum and average
total_sum = sum(arr)
average = total_sum / len(arr)
print("Sum of elements:", total_sum)
print("Average of elements:", average)
