import numpy as np
import sympy as sp
from sympy import *
# Define a matrix
A = np.array([[3, 7, 9,],[5, 2, 1,],[-2, -9, 8]])

# Perform row operations to transform A into echelon form

A_ech  = Matrix(A).rref()[0]


# Print the echelon form of A
print("Echelon form of A:")
print(A_ech)

# Find the rank of A by counting the number of non-zero rows
rank = np.linalg.matrix_rank(A.astype(np.float64))
print("Rank of A:", rank)

