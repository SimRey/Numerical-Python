import numpy as np
from gekko import GEKKO

#                                       Tubular Column Design Optimization
# The objective is to optimize the cost of building the column, using variables d, the mean diameter of the column (cm),
# and t, the thickness of the column (cm). P is the compressive load of 2300 kgf. The material used to make the column
# has a module of elasticity (E) of 0.65x106 and a weight density (ρ) of 0.0020 kgf/cm3. The column has a yield stress
# (σy) of 450 kgf/cm2 and a length (l) of 300 cm. Due to available materials the diameter must be ≤ 14.0 cm and ≥ 2.0 cm
# Similarly, the thickness must be ≤ 0.8 cm and ≥ 0.2 cm. Safety requires that the induced stress is less than the
# yield stress and that the induced stress is less than the buckling stress. The cost of the column is equal to the
# expression 5W + 2d with W being the weight in kilograms force (kgf).


# Initialize Model
m = GEKKO()

# Variables
d = m.Var(value=8.0, lb=2.0, ub=14.0)  # mean diameter (cm)
t = m.Var(value=0.3, lb=0.2, ub=0.8)  # thickness (cm)
cost = m.Var()

# Constants
pi = m.Const(np.pi, 'pi')
P = m.Const(2300)  # compressive load (kg_f)
o_y = m.Const(450)  # yield stress (kg_f/cm^2)
E = m.Const(0.65e6)  # elasticity (kg_f/cm^2)
p = m.Const(0.0020)  # weight density (kg_f/cm^3)
l = m.Const(300)  # length of the column (cm)

# Intermediate equations

di = m.Intermediate(d - t)  # inner diameter
do = m.Intermediate(d + t)  # outer diameter
W = m.Intermediate(p * l * pi * (do ** 2 - di ** 2) / 4)  # weight
I = m.Intermediate((pi / 64) * (do ** 4 - di ** 4))  # second moment
o_i = m.Intermediate(P / (pi * d * t))  # induced stress
o_b = m.Intermediate((pi ** 2 * E * I) / (pi * d * t * l ** 2))  # buckling stress

# Constrains equations
m.Equation(o_i <= o_y)
m.Equation(o_i <= o_b)
m.Equation(cost == 5 * W + 2 * d)

# Objective
m.Minimize(cost)

# Solve and print solution
m.solve()

print('Optimal cost: ' + str(cost[0]))
print('Optimal mean diameter: ' + str(d[0]))
print('Optimal thickness: ' + str(t[0]))
