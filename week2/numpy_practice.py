import numpy as np

A = np.array([
    [2, 1, 0],
    [0, 3, 1],
    [0, 0, 4]
], dtype=float)

print("Shape:", A.shape)
print("First row:", A[0, :])
print("First column:", A[:, 0])
print("Transpose:\n", A.T)  # Transposing swaps rows and columns

print("Elementwise multiplication:\n", A*A)
print("Matrix multiplication:\n", A@A)  # Using @ for matrix multiplication 

A_inverse = np.linalg.inv(A)
print("Inverse of A:\n", A_inverse)
print("A @ inverse:\n", A @ A_inverse)  # Should be close to the identity matrix   

b = np.array([4, 9, 12], dtype=float)
x = np.linalg.solve(A, b)

print("Solution x of Ax = b:\n", x)
print("Solution works:", np.allclose(A @ x, b))  # Check if Ax is close to b

#---------------

angles = np.linspace(0, np.pi, 5)  # 5 angles from 0 to pi

print("Angles:", angles)
print("Sines:", np.sin(angles))

def rot2d(theta):
    """Returns a 2D rotation matrix for an angle in radians."""

    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [c, -s],
        [s, c]
    ])

point = np.array([1, 0])
rotated = rot2d(np.pi / 2) @ point

print("Rotated point:", rotated)  # Should be close to [0, 1]
print("Done when:", np.allclose(rotated, [0, 1]))  # Check if the rotated point is close to [0, 1]