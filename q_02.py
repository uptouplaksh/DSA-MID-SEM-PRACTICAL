'''
Write a program to create an array and Perform the following operations
Append element in an array
Insert Before a Specific Index
Remove an Item by Index
Remove Duplicates from an Array
Reverse an Array
Remove duplicate elements from an array
'''

# Create an array
arr = [10, 20, 30, 40, 50, 30, 20, 10]
print("Original Array:", arr)

# i. Append element in an array
element = int(input("Enter element to append: "))
arr.append(element)
print("After Appending:", arr)

# ii. Insert Before a Specific Index
index = int(input("Enter index before which to insert: "))
value = int(input("Enter value to insert: "))
arr.insert(index, value)
print("After Inserting:", arr)

# iii. Remove an Item by Index
rem_index = int(input("Enter index to remove: "))
if 0 <= rem_index < len(arr):
    arr.pop(rem_index)
    print("After Removing by Index:", arr)
else:
    print("Invalid Index!")

# iv. Remove Duplicates from an Array
arr_no_duplicates = []
for item in arr:
    if item not in arr_no_duplicates:
        arr_no_duplicates.append(item)
print("After Removing Duplicates:", arr_no_duplicates)

# v. Reverse an Array
arr_no_duplicates.reverse()
print("Reversed Array:", arr_no_duplicates)

# vi. Remove duplicate elements from an array (same as iv, shown again for clarity)
final_arr = []
for i in arr_no_duplicates:
    if i not in final_arr:
        final_arr.append(i)
print("Final Array after Removing Duplicates Again:", final_arr)
