## Linear Programming and Randomized Algorithms

Linear programming (LP) and randomized algorithms are essential tools in optimization and simulation. LP helps optimize processes by considering constraints, widely used in industries to minimize costs and maximize production. Randomized algorithms, like the Monte Carlo method, are effective for approximate results when exact calculations are complex. This homework assignment involves two tasks: optimizing production using LP with the PuLP library and calculating a definite integral using the Monte Carlo method.

### Task Description

#### Task 1: Production Optimization

A company produces two types of beverages: "Lemonade" and "Fruit Juice". Different ingredients and limited equipment are used to produce these beverages. The goal is to maximize production, considering the limited resources.

**Task Conditions:**

- "Lemonade" is made from "Water", "Sugar", and "Lemon Juice".
- "Fruit Juice" is made from "Fruit Puree" and "Water".
- Resource constraints: 100 units of "Water", 50 units of "Sugar", 30 units of "Lemon Juice", and 40 units of "Fruit Puree".
- Producing one unit of "Lemonade" requires 2 units of "Water", 1 unit of "Sugar", and 1 unit of "Lemon Juice".
- Producing one unit of "Fruit Juice" requires 2 units of "Fruit Puree" and 1 unit of "Water".

Using PuLP, create a model that determines how much "Lemonade" and "Fruit Juice" should be produced to maximize the total quantity of products while adhering to the resource constraints. Write a program whose code maximizes the total amount of "Lemonade" and "Fruit Juice" produced, considering the resource constraints.

**Example:**

```python
import pulp

# Define the problem
prob = pulp.LpProblem("Production Optimization", pulp.LpMaximize)

# Define variables
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Continuous')

# Objective function
prob += lemonade + fruit_juice

# Constraints
prob += 2*lemonade + 1*fruit_juice <= 100  # Water constraint
prob += 1*lemonade <= 50                   # Sugar constraint
prob += 1*lemonade <= 30                   # Lemon Juice constraint
prob += 2*fruit_juice <= 40                # Fruit Puree constraint

# Solve the problem
prob.solve()

# Print the results
print(f"Lemonade: {pulp.value(lemonade)}")
print(f"Fruit Juice: {pulp.value(fruit_juice)}")
```

#### Task 2: Calculating a Definite Integral

Your second task is to calculate the value of an integral of a function using the Monte Carlo method.

**Description:**

You can choose the function yourself.

We'll start with plotting the graph.

**Example:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Define the function and integration bounds
def f(x):
    return x ** 2

a = 0  # Lower bound
b = 2  # Upper bound

# Create a range of x values
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Plot the graph
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

# Add integration bounds and title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Integration of f(x) = x^2 from {a} to {b}')
plt.grid()
plt.show()
```

This will produce the following result:

Next, compute the integral using the Monte Carlo method to find the area under this curve (gray area).

**Example:**

```python
import numpy as np

# Define the function
def f(x):
    return x**2

# Monte Carlo integration
a = 0
b = 2
n = 10000
x_random = np.random.uniform(a, b, n)
y_random = f(x_random)
integral = (b - a) * np.mean(y_random)

print("Monte Carlo Integral: ", integral)
```

Verify the accuracy of the Monte Carlo method by comparing the obtained result with analytical calculations or the result of using the `quad` function.

**Example:**

```python
import scipy.integrate as spi

# Define the function
def f(x):
    return x**2

# Define the integration bounds
a = 0
b = 2

# Calculate the integral
result, error = spi.quad(f, a, b)

print("Analytical Integral: ", result)
```

Output:

```
Analytical Integral:  2.666666666666667
```

### Results

#### Task 1: Production Optimization

After solving the linear programming model for production optimization, the results are as follows:

- **Status**: The solution status is "Optimal", indicating that the model found the best solution within the given constraints.
- **Lemonade**: The optimal quantity of Lemonade to produce is 30 units.
- **Fruit Juice**: The optimal quantity of Fruit Juice to produce is 20 units.
- **Total Products**: The total production of Lemonade and Fruit Juice combined is 50 units.

### Conclusion

By using linear programming, we have effectively optimized the production of Lemonade and Fruit Juice, considering the resource constraints. The solution maximizes the total production while adhering to the available quantities of Water, Sugar, Lemon Juice, and Fruit Puree. This approach ensures efficient use of resources and helps in making informed production decisions, showcasing the practicality and efficiency of linear programming in real-world applications.

#### Task 2: Calculating a Definite Integral

### Results and Conclusion

**Monte Carlo Integral Results for Different Numbers of Points:**

- **100 points**: 2.88
- **1000 points**: 2.6
- **10000 points**: 2.6304
- **100000 points**: 2.65936
- **1000000 points**: 2.663064

**Integral Using Quad Function**: 2.666666666666667

### Comparison

1. **Monte Carlo Method**:

   - With 100 points, the integral estimate is 2.88, which is relatively far from the exact value.
   - Increasing the number of points to 1000 improves the estimate to 2.6.
   - With 10,000 points, the estimate further improves to 2.6304.
   - With 100,000 points, the estimate becomes 2.65936, showing convergence towards the exact value.
   - With 1,000,000 points, the estimate is 2.663064, very close to the exact value of 2.666666666666667.

2. **Quad Function**:
   - The quad function provides a highly accurate result of 2.666666666666667, with a negligible error.

### Conclusion

The comparison between the Monte Carlo method and the quad function for calculating the integral of \( f(x) = x^2 \) from \( a = 0 \) to \( b = 2 \) highlights the following points:

- **Monte Carlo Method**:

  - Provides approximate results that improve with the number of random points used.
  - For small numbers of points (e.g., 100 or 1000), the estimates can be relatively inaccurate.
  - As the number of points increases (e.g., 1,000,000), the estimates converge to the exact value, demonstrating the effectiveness of the Monte Carlo method for large sample sizes.
  - Suitable for complex functions or higher-dimensional integrals where traditional methods might struggle.

- **Quad Function**:
  - Provides an exact and highly accurate result with minimal error.
  - Ideal for well-behaved, lower-dimensional integrals.

**Overall**, while the Monte Carlo method is useful for approximation and handles complexity well, the quad function is superior in accuracy and precision for simpler, well-defined integrals. The Monte Carlo method's accuracy improves significantly with larger sample sizes, making it a valuable tool when analytical solutions are not feasible.
