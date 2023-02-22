import numpy as np

# Define the vector field
def vector_field(x, y, z):
    return np.array([y*z, -x*z, x*y])

# Define the partial derivative function for x
def partial_x(f, x, y, z, h):
    return (f(x+h, y, z) - f(x-h, y, z)) / (2*h)

# Define the partial derivative function for y
def partial_y(f, x, y, z, h):
    return (f(x, y+h, z) - f(x, y-h, z)) / (2*h)

# Define the partial derivative function for z
def partial_z(f, x, y, z, h):
    return (f(x, y, z+h) - f(x, y, z-h)) / (2*h)

# Define the curl function
def curl(f, x, y, z, h):
    curl_x = partial_z(f[1], x, y, z, h) - partial_y(f[2], x, y, z, h)
    curl_y = partial_x(f[2], x, y, z, h) - partial_z(f[0], x, y, z, h)
    curl_z = partial_y(f[0], x, y, z, h) - partial_x(f[1], x, y, z, h)
    return np.array([curl_x, curl_y, curl_z])

# Compute the curl of the vector field at the point (1, 2, 3) with step size 0.001
point = np.array([1, 2, 3])
h = 0.001
curl_vec = curl(vector_field(point[0], point[1], point[2]), point[0], point[1], point[2], h)

print("Curl of the vector field at point", point, ":", curl_vec)

# mehul version
import sympy as sp
print("\n CURL OF THE MATRIX\n")

# Define the symbols
x, y, z = sp.symbols('x y z')

# Define the vector field
A = sp.Matrix([x*z**3, -2*x**2*y*z, 2*y*z**4])

# Compute the curl of the vector field
curl_A = sp.Matrix([sp.diff(A[2], y) - sp.diff(A[1], z),
                    sp.diff(A[0], z) - sp.diff(A[2], x),
                    sp.diff(A[1], x) - sp.diff(A[0], y)])

curl_A.simplify()
print("The curl of the vector field {} is: \n".format(A))
print(curl_A)