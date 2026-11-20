New assumptions
Object is a unit square centred at origin.

Transformation scales by 2 and rotates 30° (was 45°).

Row-vector convention (multiply by transpose).

Input data
4 corner points of unit square, rotation angle = π/6.

Output
text
Original points:
 [[0. 0.]
  [1. 0.]
  [1. 1.]
  [0. 1.]]
Transformation matrix:
 [[ 1.732 -1.   ]
  [ 1.     1.732]]
Transformed points:
 [[0.    0.   ]
  [1.732 1.   ]
  [0.732 2.732]
  [-1.    1.732]]
Determinant: 4.000000000000001
Interpretation
Reducing the angle from 45° to 30° gives a less rotated square: the [1,0] corner now lands at (1.73, 1.0) instead of (1.41, 1.41). The determinant is still 4 because scaling factor 2² = 4 and rotation preserves area — confirming that rotation does not affect determinant, only scale does.
