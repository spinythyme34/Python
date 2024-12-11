import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C_add = np.add(A, B)
C_sub = np.subtract(A, B)
C_mul = np.multiply(A, B)

C_dot = np.dot(A, B)

print("Matrix Addition:")
print(C_add)

print("\nMatrix Subtraction:")
print(C_sub)

print("\nMatrix Multiplication (Element-wise):")
print(C_mul)

print("\nMatrix Multiplication (Dot Product):")
print(C_dot)
