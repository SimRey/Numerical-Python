import numpy as np
from gekko import GEKKO

#                                           Tsiolkovsky Rocket Optimization
# The Tsiolkovsky rocket has a direct correlation between the change of velocity  (Δv) of a rocket, wet mass (m0),
# dry mass (mf), and exhaust velocity (v0).
# This problem optimizes the design of a simple rocket for profit. Potential revenue increases with greater change in
# velocity, as greater velocities allow the payload to reach higher orbits that have less drag, allowing it to remain
# in orbit longer. Wet mass, dry mass, and exhaust velocity are design variables, where wet mass is the total initial
# mass of the rocket, including propellant, and dry mass is the mass of the rocket at full ascent.

# The rocket must have a dry mass of at least 20,000 kilograms and the change in velocity should be between 9,400 m/s
# and 20,200 meters per second. Varying designs allow for exhaust velocities ranging from 2,500 m/s to 4,500 m/s.
# An appropriate guess value for the wet mass is 150,650 kilograms.

# Initialize Model
m = GEKKO()

# Variables
mf = m.Var(lb=20000)
m0 = m.Var(150650)
v0 = m.Var(lb=2500, ub=4500)
dv = m.Var(lb=9400, ub=202000)
profit = m.Var()

# Intermediate equations

Cf = m.Intermediate(4.154*(m0-mf))
Cd = m.Intermediate(154.36*mf)
Cex = m.Intermediate(75*v0)
R = m.Intermediate(550*dv)

# Constrains equations
m.Equation(dv == v0*m.log(m0/mf))
m.Equation(2*mf <= m0)
m.Equation(profit == R - (Cf+Cd+Cex))

# Objective
m.Maximize(profit)

# Solve and print solution
m.solve()

print(f'Profit: {profit[0]}')


