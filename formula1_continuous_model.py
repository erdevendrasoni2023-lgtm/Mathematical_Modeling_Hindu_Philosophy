import matplotlib.pyplot as plt
import numpy as np

# Define the function f(t)
def f(t):
    return t / (1 + t)

# Create a range of values for 't' (Manifestation Intensity)
# We go from 0 to 10 to see the curve clearly approaching 1.
t_values = np.linspace(0, 10, 500)

# Calculate the 'f(t)' values (Degree of Unity)
ft_values = f(t_values)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the continuous curve
plt.plot(t_values, ft_values, label='f(t) = t / (1 + t)', color='blue')

# Add a horizontal line at y=1 to show the asymptotic limit (Saguna)
plt.axhline(y=1, color='gray', linestyle='--', label='Saguna (Limit as t -> ∞)')

# Add a point at the origin (t=0) to represent Nirguna
plt.plot(0, 0, 'ro', label='Nirguna (t=0)')

# Add labels and title for clarity
plt.title('Visualization of Continuous Model: Nirguna to Saguna')
plt.xlabel('t (Manifestation Intensity)')
plt.ylabel('f(t) (Degree of Unity)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Save the plot (optional)
# plt.savefig("continuous_model_graph.png")

# Show the plot
plt.show()
