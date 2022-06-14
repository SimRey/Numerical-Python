# Linear equations
from scipy import linalg as la
import numpy as np
import sympy as sym

A = np.array([[2, 3], [5, 4]])
b = np.array([4, 3])
x = la.solve(A, b)
print(x)
print()
# Another way to do it is:
xx = np.dot(np.linalg.inv(A), b)
print(xx)
print()
print()
# ----------------------------------------------------------------------------------------------------------------
# Symbolic solving
xx, yy = sym.symbols("xx, yy")
ans = sym.linsolve([2 * xx + 3 * yy - 4, 5 * xx + 4 * yy - 3], (xx, yy))
print(ans)

p = sym.symbols("p", positive=True)
A2 = sym.Matrix([[1, sym.sqrt(p)], [1, 1 / sym.sqrt(p)]])
b2 = sym.Matrix([1, 2])

xp = A2.solve(b2)
print(xp)

# ---------------------------------------------------------------------------------------------------------------
# Rectangular systems --> over or under determined

# Underdetermined (more variables than equations)

x_vars = sym.symbols("x1, x2, x3")
a_under = sym.Matrix([[1, 2, 3], [4, 5, 6]])
x_under = sym.Matrix(x_vars)
b_under = sym.Matrix([7, 8])

f = a_under * x_under - b_under
sol = sym.solve(f, x_vars)
print(sol)

print()
print()
# --------------------------------------------------------------------------------------------------------------
# Eigenvalues and eigenvectors

A_eigen = np.array([[7, 3], [3, -1]])
evals, evecs = la.eig(A_eigen)
print(evals)
print(evecs)
