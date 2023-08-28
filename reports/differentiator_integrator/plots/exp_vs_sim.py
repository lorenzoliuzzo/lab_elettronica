import os
import numpy as np
import matplotlib.pyplot as plt

# Define the target circuit
target = 'differentiator'
# target = 'integrator'

# Define the directory paths
output_dir = '../data'  # Update this to your desired output directory

# Read experimental data from combined file
combined_data = np.loadtxt(os.path.join(output_dir, target + '.txt'))
exp_frequencies = combined_data[:, 0]
exp_gain = combined_data[:, 1]
exp_phase = combined_data[:, 2]

# Read simulated data from file
simulated_data = np.loadtxt(os.path.join(output_dir, 'simulated/' + target + '.txt'))
sim_frequencies = simulated_data[:, 0]
sim_gain = simulated_data[:, 1]
sim_phase = simulated_data[:, 2]

# Create a single plot for Gain
plt.figure(figsize=(10, 6))
plt.semilogx(exp_frequencies, exp_gain, marker='o', color='tab:blue', label='Experimental Gain')
plt.semilogx(sim_frequencies, sim_gain, linestyle='--', color='tab:red', label='Simulated Gain')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain [dB]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.title('Experimental vs Simulated Gain - Differentiator Circuit')
# plt.title('Experimental vs Simulated Gain - Integrator Circuit')
plt.tight_layout()

# Save the plot
output_path_gain = '../figures/' + target + '/gain_plot.png'
os.makedirs(os.path.dirname(output_path_gain), exist_ok=True)
plt.savefig(output_path_gain)
plt.close()

# Create a single plot for Phase
plt.figure(figsize=(10, 6))
plt.semilogx(exp_frequencies, exp_phase, marker='o', color='tab:blue', label='Experimental Phase')
plt.semilogx(sim_frequencies, sim_phase, linestyle='--', color='tab:red', label='Simulated Phase')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [rad]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.title('Experimental vs Simulated Phase - Differentiator Circuit')
# plt.title('Experimental vs Simulated Phase - Integrator Circuit')
plt.tight_layout()

# Save the plot
output_path_phase = '../figures/' + target + '/phase_plot.png'
os.makedirs(os.path.dirname(output_path_phase), exist_ok=True)
plt.savefig(output_path_phase)
plt.close()
