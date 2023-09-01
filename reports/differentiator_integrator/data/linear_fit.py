import numpy as np

# Data input
# input = 'differentitor.txt' 
input = 'simulated/differentiator.txt'
# input = 'integrator.txt' 
# input = 'simulated/integrator.txt'

# Circuit parameters
R = 9.94e3
C = 2.27e-9

# Frequency range
f_min = 1e2
f_max = 1e4

# Calculate the cutoff frequency
f_c = 1 / (2 * np.pi * R * C)

# Load only the first two columns
data = np.loadtxt(input, usecols=(0, 1))  
x_data_full = data[:, 0]
y_data_full = data[:, 1]

# Find the indices where x_data is within the subinterval
indices_subinterval = np.where((x_data_full >= f_min) & (x_data_full <= f_max))

# Extract the subinterval of data
x_data = np.log10(x_data_full[indices_subinterval])
y_data = y_data_full[indices_subinterval]

# Target value to interpolate
y_target = 0.0

# Perform polynomial interpolation
coefficients = np.polyfit(x_data, y_data, 1)

# Calculate the interpolated frequency
interpolated_frequency = 10 ** (-coefficients[1]/ coefficients[0])

# Calculate the delta
delta = np.abs(interpolated_frequency - f_c)

# Print the results
print('Input file:', input)
print('Number of data points:', len(x_data))
print('Frequency range:', f_min, 'Hz to', f_max, 'Hz')
print('Target Gain:', y_target, 'dB')
print('Cutoff frequency:', f_c)
print()
print('np.polyfit() coefficients:', coefficients)
print('Interpolated frequency:', interpolated_frequency)
print('Delta:', delta)
print('Error:', delta / f_c * 100, '%')