New assumptions
Added edge A–D so the network becomes a fully connected 4-node graph (each node connects to 3 others).

Undirected, unweighted graph.

Input data
4×4 adjacency matrix of the complete graph K4.

Output
text
All eigenvalues: [ 3. -1. -1. -1.]
Dominant eigenvalue: 3.0
Node centrality (normalized):
  A: 0.2500
  B: 0.2500
  C: 0.2500
  D: 0.2500
Interpretation
Adding the A–D edge makes the graph perfectly symmetric, so all four nodes now score exactly 0.25 — no node is more influential. In the original network (edge missing), B and C scored highest; the comparison shows that eigenvector centrality is highly sensitive to which connections exist.
