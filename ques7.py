import numpy as np

# Check linear dependence of vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

matrix = np.array([v1, v2, v3])

if np.linalg.matrix_rank(matrix) < matrix.shape[0]:
    print("The vectors are linearly dependent")
else:
    print("The vectors are linearly independent")

# Generate linear combination of vectors
coefficients = np.array([2, -1, 3])
linear_combination = coefficients.dot(matrix)

print("Linear combination of vectors:", linear_combination)

# Find transition matrix of matrix space
M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[0, 1], [1, 0]])
M3 = np.array([[2, 0], [0, 2]])

matrix_space = np.array([M1, M2, M3])

basis = []
for matrix in matrix_space:
    if np.linalg.matrix_rank(matrix) == matrix.shape[0]:
        basis.append(matrix)

transition_matrix = np.column_stack(basis)

print("Transition matrix of matrix space:")
print(transition_matrix)
