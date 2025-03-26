import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

# Number sets for x & y
# Choose either random, or already defined
n = randint(3, 12)
x = [a for a in range(n)]
y = [randint(-10, 10) for a in range(n)]
# x = [1,2,3,4,5,6,7]
# y = [2,1,-3,5,8,-6,7]

# X-Axis
xAxis = np.linspace(min(x)-0.25, max(x)+0.25, 100)

# Lagrange Interpolation Equation
# P(x) = Σ{n, i=1}(yi * L(x))
# L(x) = ∏{j≠i}((x - xj) / (xi - xj))

P = 0
for k in range(len(x)):
    L = 1 # Set L to 1 so the graph won't be 0
    for i in range(len(x)):
        if x[k] != x[i]:
            L *= (xAxis - x[i]) / (x[k] - x[i])
    # Plotting the individual Lagrange Equations
    plt.plot(xAxis, L, linestyle=':')
    P += y[k] * L

# Set Axis & guideline at y=1
plt.axhline(y=1, color='black', linewidth=0.5, linestyle='--')
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)

# Plot the Lagrange equation & plot points
plt.plot(xAxis, P, color='blue')
plt.scatter(x, y, color='red')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Equation Plot')

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.show()
