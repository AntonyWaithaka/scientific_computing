import numpy as np
from scipy.interpolate import interp1d, CubicSpline

# Added one more calibration point at ADC=1300
adc  = np.array([200, 400, 600, 800, 1000, 1200, 1300])
temp = np.array([10.0, 25.0, 40.0, 55.0, 70.0, 85.0, 92.5])

linear = interp1d(adc, temp, kind='linear')
cubic  = CubicSpline(adc, temp)

test_adc = np.array([300, 500, 700, 900, 1100, 1250])
print("ADC    Linear   Cubic")
for a in test_adc:
    print(f"{a:5d}  {linear(a):6.2f}  {cubic(a):6.2f}")
