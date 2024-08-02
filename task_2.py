import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Define the function and integration limits
def f(x):
    return x ** 2

a = 0  # Lower limit
b = 2  # Upper limit

# Function to calculate Monte Carlo integral
def monte_carlo_integral(n_points, a, b):
    x_rand = np.random.uniform(a, b, n_points)
    y_rand = np.random.uniform(0, f(b), n_points)
    n_points_under_curve = np.sum(y_rand <= f(x_rand))
    integral_mc = (n_points_under_curve / n_points) * (b - a) * f(b)
    return integral_mc

# Monte Carlo integrals for different numbers of points
integrals_mc = {}
for n in [100, 1000, 10000, 100000, 1000000]:
    integrals_mc[n] = monte_carlo_integral(n, a, b)

# Print Monte Carlo results
for n, integral in integrals_mc.items():
    print(f"Monte Carlo integral ({n} points): {integral}")

# Calculate the integral using quad
result, error = spi.quad(f, a, b)
print("Integral using quad: ", result)

# Create a range of x values
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Create a plot
fig, ax = plt.subplots()

# Plot the function
ax.plot(x, y, 'r', linewidth=2)

# Fill the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Set plot limits and labels
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Add integration limits and title to the plot
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Plot of the integral of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()