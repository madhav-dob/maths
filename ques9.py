import numpy as np

# Define a matrix
A = np.array([[2, 1], [4, 3]])

# Find the eigenvalues and eigenvectors of the matrix
eigenvalues, eigenvectors = np.linalg.eig(A)

# Check if the matrix is diagonalizable
if np.all(np.isreal(eigenvalues)) and np.linalg.matrix_rank(eigenvectors) == A.shape[0]:
    print("The matrix is diagonalizable.")
else:
    print("The matrix is not diagonalizable.")

# Print the eigenvalues and eigenvectors
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Verify the Cayley-Hamilton theorem
I = np.eye(A.shape[0])
p_A = np.poly(A)
if np.allclose(p_A, np.zeros_like(A)):
    print("The Cayley-Hamilton theorem holds.")
else:
    print("The Cayley-Hamilton theorem does not hold.")
