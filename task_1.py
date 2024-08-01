import pulp

# Create a linear programming model
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Define variables
x = pulp.LpVariable("Lemonade", lowBound=0)  # Quantity of Lemonade to produce
y = pulp.LpVariable("FruitJuice", lowBound=0)  # Quantity of Fruit Juice to produce

# Add resource constraints
model += (2 * x + y <= 100, "Water_Constraint")  # Water constraint
model += (x <= 50, "Sugar_Constraint")  # Sugar constraint
model += (x <= 30, "LemonJuice_Constraint")  # Lemon Juice constraint
model += (2 * y <= 40, "FruitPuree_Constraint")  # Fruit Puree constraint

# Define objective function
model += x + y  # Maximize total production

# Solve the problem
model.solve()

# Print results
print(f"Status: {pulp.LpStatus[model.status]}")  # Print solution status
print(f"Lemonade: {pulp.value(x)}")  # Print optimal quantity of Lemonade
print(f"FruitJuice: {pulp.value(y)}")  # Print optimal quantity of Fruit Juice
print(f"Total Products: {pulp.value(model.objective)}")  # Print total production