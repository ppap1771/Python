import numpy as np

# Create tensors with unequal ndim
A = np.array([1, 2, 3])  # Shape: (3,)
B = np.array([[4, 5, 6], [7, 8, 9]])  # Shape: (2, 3)

# Expand dimensions of A to match the shape of B
A_expanded = np.expand_dims(A, axis=0)  # Shape: (1, 3)

# Perform element-wise multiplication
product = A_expanded * B  # Shape: (2, 3)

# Sum the result along the first axis
dot_product = np.sum(product, axis=1)  # Shape: (2,)

print(dot_product)
