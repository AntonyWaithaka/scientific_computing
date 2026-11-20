import numpy as np

# Four corners of a unit square
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Changed rotation from 45° to 30° for comparison
theta = np.pi / 6            # 30 degrees
scale = np.diag([2.0, 2.0])
rotation = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])
transformation = rotation @ scale

# Row-vector convention: multiply by transpose
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))
