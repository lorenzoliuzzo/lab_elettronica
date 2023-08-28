import os
import numpy as np
import matplotlib.pyplot as plt

# Define the target circuit
target = 'differentiator'
# target = 'integrator'

# Define the directory paths
output_dir = '../data'  # Update this to your desired output directory

# Read data from combined file
combined_data = np.loadtxt(os.path.join(output_dir, target + '.txt'))

frequencies = combined_data[:, 0]
gain = combined_data[:, 1]
phase = combined_data[:, 2]

# Create a single plot with two y-axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting Gain on the primary y-axis (ax1)
line1, = ax1.semilogx(frequencies, gain, marker='o', color='tab:blue', label='Circuit Gain')
ax1.set_xlabel('Frequency [Hz]', color='black')
ax1.set_ylabel('Gain [dB]', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True, which="both", ls="--")

# Creating a secondary y-axis for Phase on the same plot
ax2 = ax1.twinx()
line2, = ax2.semilogx(frequencies, phase, marker='x', color='tab:orange', label='Circuit Phase')
ax2.set_ylabel('Phase [rad]', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Combine legend for both lines
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper right')

plt.title('Bode Plot - Differentiator Circuit')
# plt.title('Bode Plot - Integrator Circuit')
plt.tight_layout()

# Save the plot
output_path = '../figures/' + target + '/bode_plot.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
plt.close()