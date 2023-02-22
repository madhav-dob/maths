import numpy as np

# Define a function to solve a system of linear equations using Gauss elimination
def gauss_elimination(A, b):
    n = len(b)

    # Combine matrix A and vector b into a single augmented matrix
    M = np.concatenate((A, b.reshape(n, 1)), axis=1)

    # Elimination phase
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:n+1] = M[i, k:n+1] - factor * M[k, k:n+1]

    # Back-substitution phase
    x = np.zeros(n)
    x[n-1] = M[n-1, n] / M[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]

    return x

# Example 1: Solving a system of homogeneous equations
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.zeros(3)
x = gauss_elimination(A, b)
print("Example 1 - Homogeneous equations:")
print("Solution:", x)

# Example 2: Solving a system of non-homogeneous equations
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 2, 3])
x = gauss_elimination(A, b)
print("Example 2 - Non-homogeneous equations:")
print("Solution:", x)
