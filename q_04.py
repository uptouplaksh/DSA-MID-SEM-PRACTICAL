# Write a python program of sparse matrix REPRESENTATION for 3-tuple method using array

# Python program to represent a Sparse Matrix using 3-Tuple method

# Original Matrix (you can change values or take user input)
matrix = [
    [0, 0, 3],
    [0, 0, 0],
    [4, 0, 5]
]

rows = len(matrix)
cols = len(matrix[0])

# Count non-zero elements
non_zero = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            non_zero += 1

# Create the 3-tuple representation array
# First row: [number of rows, number of columns, number of non-zero elements]
sparse = []
sparse.append([rows, cols, non_zero])

# Fill in row, column, and value for each non-zero element
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            sparse.append([i, j, matrix[i][j]])

# Display the 3-tuple representation
print("Sparse Matrix Representation (3-Tuple Format):")
for row in sparse:
    print(row)
