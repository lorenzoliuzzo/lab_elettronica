import os
import numpy as np
import matplotlib.pyplot as plt

# Define the target circuit
# target = 'differentiator'
target = 'integrator'

# Define the directory paths
output_dir = '../data'  # Update this to your desired output directory

# Read data from combined file
combined_data = np.loadtxt(os.path.join(output_dir, target + '.txt'))

gain = np.abs(combined_data[:, 1])
phase = combined_data[:, 2]

plt.figure(figsize=(10, 6))
plt.polar(phase, gain)
# plt.xlabel('Real')
# plt.ylabel('Imaginary')
plt.grid(True, which="both", ls="--")
# plt.title('Nyquist Plot - Differentiator Circuit')
plt.title('Nyquist Plot - Integrator Circuit')
plt.tight_layout()

# Save the plot
output_path = '../figures/' + target + '/nyquist_plot.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
plt.close()