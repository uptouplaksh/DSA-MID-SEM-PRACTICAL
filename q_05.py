# Write a python program to add sparse matrices.

# Function to convert a normal matrix into sparse (3-tuple) form
def to_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sparse = []
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])
                count += 1
    # Add header [rows, cols, non-zero count]
    sparse.insert(0, [rows, cols, count])
    return sparse


# Function to add two sparse matrices
def add_sparse(s1, s2):
    if s1[0][0] != s2[0][0] or s1[0][1] != s2[0][1]:
        print("Addition not possible — Matrices dimensions do not match.")
        return []

    result = [[s1[0][0], s1[0][1], 0]]  # Header placeholder
    i, j = 1, 1  # start from 1 because 0th row is header

    while i <= s1[0][2] and j <= s2[0][2]:
        if s1[i][0] == s2[j][0] and s1[i][1] == s2[j][1]:
            result.append([s1[i][0], s1[i][1], s1[i][2] + s2[j][2]])
            i += 1
            j += 1
        elif (s1[i][0] < s2[j][0]) or (s1[i][0] == s2[j][0] and s1[i][1] < s2[j][1]):
            result.append(s1[i])
            i += 1
        else:
            result.append(s2[j])
            j += 1

    # Add remaining elements
    while i <= s1[0][2]:
        result.append(s1[i])
        i += 1
    while j <= s2[0][2]:
        result.append(s2[j])
        j += 1

    # Update header with new count
    result[0][2] = len(result) - 1
    return result


# Example matrices
A = [
    [0, 0, 3],
    [4, 0, 0],
    [0, 5, 0]
]

B = [
    [0, 2, 0],
    [4, 0, 6],
    [0, 0, 0]
]

# Convert to sparse form
sparse_A = to_sparse(A)
sparse_B = to_sparse(B)

print("Sparse Matrix A:")
for row in sparse_A:
    print(row)

print("\nSparse Matrix B:")
for row in sparse_B:
    print(row)

# Add both sparse matrices
result_sparse = add_sparse(sparse_A, sparse_B)

print("\nResultant Sparse Matrix (A + B):")
for row in result_sparse:
    print(row)
