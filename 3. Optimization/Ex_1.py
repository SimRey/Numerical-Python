from scipy import optimize as opt
import numpy as np


# APMonitor example

def f(var):
    x1 = var[0]
    x2 = var[1]
    x3 = var[2]
    x4 = var[3]
    return x1 * x4 * (x1 + x2 + x3) + x3


def con1(var):
    x1 = var[0]
    x2 = var[1]
    x3 = var[2]
    x4 = var[3]
    return x1 * x2 * x3 * x4 - 25


def con2(var):
    x1 = var[0]
    x2 = var[1]
    x3 = var[2]
    x4 = var[3]
    return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 - 40


cons1 = dict(type='ineq', fun=con1)
cons2 = dict(type='eq', fun=con2)
cons = [cons1, cons2]

b = (1, 5)
bound = [b, b, b, b]
x0 = np.array([1, 5, 5, 1])

x_cons_opt_2 = opt.minimize(f, x0, method='SLSQP', constraints=cons, bounds=bound)
print(x_cons_opt_2.x)

print()
print()

# Gekko script
from gekko import GEKKO

# Initialize Model
m = GEKKO()



# initialize variables
x1, x2, x3, x4 = [m.Var() for i in range(4)]

# initial values
x1.value = x4.value = 1
x2.value = x3.value = 5

# lower bounds
x1.lower = x2.lower = x3.lower = x4.lower = 1

# upper bounds
x1.upper = x2.upper = x3.upper = x4.upper = 5

# Constrains
m.Equation(x1 * x2 * x3 * x4 >= 25)
m.Equation(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 == 40)

# Objective
m.Obj(x1 * x4 * (x1 + x2 + x3) + x3)

# Set global options
m.options.IMODE = 3  # steady state optimization

# Solve simulation
m.solve()

# Results
print('')
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('x3: ' + str(x3.value))
print('x4: ' + str(x4.value))
