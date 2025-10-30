# Write a python program to check whether a given matrix is sparse or not.

# Python program to check if a matrix is sparse or not

# Input matrix (you can change values or take input dynamically)
matrix = [
    [0, 0, 3],
    [0, 0, 0],
    [4, 0, 0]
]

rows = len(matrix)
cols = len(matrix[0])
total_elements = rows * cols

# Count zeros
zero_count = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_count += 1

# Check if sparse
if zero_count > (total_elements / 2):
    print("The given matrix is a Sparse Matrix.")
else:
    print("The given matrix is NOT a Sparse Matrix.")

print(f"Total Elements: {total_elements}")
print(f"Zero Elements: {zero_count}")
