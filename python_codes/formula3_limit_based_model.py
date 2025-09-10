import matplotlib.pyplot as plt
import numpy as np

# Create the plot
plt.figure(figsize=(10, 6))

# 1. Plot a line for Nirguna (0)
x_values = np.linspace(0, 10, 50)
y_values_nirguna = np.zeros_like(x_values)
plt.plot(x_values, y_values_nirguna, 'b--', label='Nirguna (0)', linewidth=2)
plt.text(5, 0.2, 'Nirguna (0)', fontsize=12, ha='center', color='blue')

# 2. Plot a line for Saguna (1)
y_values_saguna = np.ones_like(x_values)
plt.plot(x_values, y_values_saguna, 'g--', label='Saguna (1)', linewidth=2)
# The y-coordinate has been corrected to 1.2
plt.text(5, 1.2, 'Saguna (1)', fontsize=12, ha='center', color='green')

# 3. Plot a line for Anant (∞)
y_values_anant = x_values
plt.plot(x_values, y_values_anant, 'r-', label='Anant (∞)', linewidth=2)
plt.text(8, 8, 'Anant (∞)', fontsize=12, ha='center', color='red')

# Add a title and labels
plt.title('Visualization of Nirguna (0), Saguna (1), and Anant (∞)')
plt.xlabel('Conceptual Space')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Save the plot
plt.savefig("formula_3_graph.png")

# Show the plot
plt.show()
