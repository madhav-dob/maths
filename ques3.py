import numpy as np

# Define a matrix
A = np.array([[2, 1, 3],
               [4, 0, 1], 
               [2, 5, 1]])

# Calculate the determinant of A
det_A = np.linalg.det(A)
print("Determinant of A: ", det_A)

# Calculate the adjoint matrix of A
adj_A = np.linalg.inv(A)* det_A
print("Adjoint matrix of A: ")
print(adj_A)


# Calculate the cofactor matrix of A
cofactor_A = adj_A.T
print("Cofactor matrix of A: ")
print(cofactor_A)


# Calculate the inverse matrix of A
inv_A = np.linalg.inv(A)
print("Inverse of A: ")
print(inv_A)

