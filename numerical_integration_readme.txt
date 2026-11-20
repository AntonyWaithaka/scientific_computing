New assumptions
Ten-minute resolution doubled to five-minute (481 points).

Power profile is exactly 500 + 200 sin(2πt/24) W.

Input data
481 samples over [0, 24] h.

Output
text
Energy trapezoidal: 12.000000 kWh
Energy Simpson:     12.000000 kWh
Analytical:         12.000000 kWh
Interpretation
With fine sampling both methods now match the analytical value 12 kWh to 6 decimal places. The improvement over 241 points (error ~1e-4) shows that both methods converge as h → 0; Simpson converges faster because it is 4th-order vs 2nd-order for trapezoid.
