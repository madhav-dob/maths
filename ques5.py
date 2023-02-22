import numpy as np

# Define the system of equations as a matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Augment the matrix with a zero vector
A_aug = np.hstack([A, np.zeros((A.shape[0], 1))])

# Perform Gauss Jordan elimination
for i in range(A_aug.shape[0]):
    # Divide the ith row by the ith diagonal element
    A_aug[i, :] = A_aug[i, :] / A_aug[i, i]
    
    # Subtract the ith row from all other rows to zero out the ith column
    for j in range(A_aug.shape[0]):
        if i != j:
            A_aug[j, :] = A_aug[j, :] - A_aug[j, i] * A_aug[i, :]
            
# Extract the solutions from the augmented matrix
x = A_aug[:, -1]

print("Solution vector:", x)
