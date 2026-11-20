import numpy as np

# Added edge A-D (was missing) -> different centrality ranking
A = np.array([
    [0., 1., 1., 1.],   # A now connects to D
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [1., 1., 1., 0.]    # D now connects to A
])

eigenvalues, eigenvectors = np.linalg.eig(A)
idx = np.argmax(np.real(eigenvalues))
dominant_value  = np.real(eigenvalues[idx])
dominant_vector = np.real(eigenvectors[:, idx])
centrality = dominant_vector / np.sum(dominant_vector)

print("All eigenvalues:", eigenvalues)
print("Dominant eigenvalue:", dominant_value)
print("Node centrality (normalized):")
for node, score in zip(["A", "B", "C", "D"], centrality):
    print(f"  {node}: {score:.4f}")
