import numpy as np
import matplotlib.pyplot as plt

# Function define with error handling
def f_continuous(t):
    if t == -1:  # Singularity point
        return float('inf')  # Infinite value
    try:
        return t / (1 + t)
    except ZeroDivisionError:
        return float('inf')  # Safety for edge cases

# Create t values, avoiding exact -1
t_values = np.linspace(-2, 2, 1000)  # Range from -2 to 2
t_values = t_values[t_values != -1]  # Remove -1 to avoid direct division by zero

# Calculate f(t) for all t values
f_values = [f_continuous(t) for t in t_values]

# Plot the graph
plt.plot(t_values, f_values, label='f(t) = t/(1+t)')
plt.axvline(x=-1, color='r', linestyle='--', label='Singularity at t=-1')
plt.title('Continuous Model with Singularity at t=-1')
plt.xlabel('t (Time/Parameter)')
plt.ylabel('f(t) (Unity Degree)')
plt.legend()
plt.grid(True)
plt.show()  # Pydroid mein yeh graph dikha dega

# Print some key points
print(f"f(-0.99) = {f_continuous(-0.99)}")  # Near singularity
print(f"f(-0.5) = {f_continuous(-0.5)}")    # Negative value
print(f"f(0) = {f_continuous(0)}")          # Zero point