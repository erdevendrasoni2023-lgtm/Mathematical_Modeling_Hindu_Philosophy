import matplotlib.pyplot as plt
import numpy as np

# 1. Continuous Model: f(t) = t / (1 + t)
t = np.linspace(0, 10, 500)
ft = t / (1 + t)

# 2. Discrete Model: A_n = 2^(n-1) for n >= 2, and A_0 = 0, A_1 = 1
n = np.array([0, 1, 2, 3, 4, 5, 6, 7])
An = np.zeros_like(n, dtype=float)
An[0] = 0
An[1] = 1
An[2:] = 2**(n[2:] - 1)

# 3. Plotting the Models
plt.figure(figsize=(10, 6))
plt.plot(t, ft, label='Continuous Model: $f(t) = \\frac{t}{1+t}$', color='blue')
plt.plot(n, An, 'o--', label='Discrete Model: $A_n$', color='red')

# 4. Adding Labels and Title for Clarity
plt.title('Integration of Continuous and Discrete Models')
plt.xlabel('Time (t) / Step (n)')
plt.ylabel('Value')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig("my_graph.png")

# Show the plot
plt.show()
