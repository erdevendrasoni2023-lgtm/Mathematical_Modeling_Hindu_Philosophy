import matplotlib.pyplot as plt
import numpy as np

# Define the range for 'n' (Creation Step)
# We start from 0 to visualize Nirguna and Saguna, then the exponential growth.
n_values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculate the A_n values based on the formula:
# A_0 = 0 (Nirguna)
# A_1 = 1 (Saguna)
# A_n = 2^(n-1) for n >= 2
An_values = np.zeros_like(n_values, dtype=float) # Initialize with zeros

An_values[0] = 0  # For n=0 (Nirguna)
An_values[1] = 1  # For n=1 (Saguna)

# Calculate for n >= 2
for i in range(2, len(n_values)):
    An_values[i] = 2**(n_values[i] - 1)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the discrete points and connect them with a dashed line
plt.plot(n_values, An_values, 'o--', label='Discrete Model: $A_n$', color='red')

# Highlight Nirguna and Saguna points
plt.plot(0, 0, 'go', markersize=8, label='Nirguna ($A_0=0$)') # Green dot for Nirguna
plt.plot(1, 1, 'bo', markersize=8, label='Saguna ($A_1=1$)') # Blue dot for Saguna


# Add labels and title for clarity
plt.title('Visualization of Discrete Model: Saguna to Anant')
plt.xlabel('n (Creation Step)')
plt.ylabel('$A_n$ (Manifestation Magnitude)')
plt.xticks(n_values) # Ensure x-axis shows discrete steps
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Save the plot (optional)
# plt.savefig("discrete_model_graph.png")

# Show the plot
plt.show()
