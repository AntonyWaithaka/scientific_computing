New assumptions
Calibration table extended to 7 points (ADC 1300 → 92.5 °C).

Interpolation is used strictly inside the calibrated range (no extrapolation).

Input data
ADC ↔ temperature pairs as shown above.

Output
text
ADC    Linear   Cubic
  300   17.50   17.50
  500   32.50   32.50
  700   47.50   47.50
  900   62.50   62.50
 1100   77.50   77.50
 1250   88.75   88.75
Interpretation
Because the added point preserves linearity (92.5 °C at 1300 is exactly the linear continuation), both methods give identical values. In practice, adding a nonlinear calibration point would cause cubic to differ from linear at midpoints — the extra point makes the fit more accurate within the range.
