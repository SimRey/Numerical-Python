import numpy as np
import cvxopt

#                                                    Simplex
# Linear programming problems are typically written in the so-called standard form: min_x c^T x where Ax ≤ b and x ≥ 0.
# Here c and x are vectors of length n, and A is a m × n matrix and b a m-vector.

# Example:
# f (x) = − x0+2x1 − 3x2, subject to the three inequality constraints x0+x1 ≤ 1, −x0+3x1 ≤ 2, and −x1+x2 ≤ 3.

c = np.array([-1.0, 2.0, -3.0])  # objective function
A = np.array([[1.0, 1.0, 0.0], [-1.0, 3.0, 0.0], [0.0, -1.0, 1.0]])  # constrains
b = np.array([1.0, 2.0, 3.0])  # equalities of constrains

A_ = cvxopt.matrix(A)
b_ = cvxopt.matrix(b)
c_ = cvxopt.matrix(c)

sol = cvxopt.solvers.lp(c_, A_, b_)
print(sol)
print(np.array(sol['x']))

print()
print()

# Maximization example:

obj_fun = np.array([-7.0, -2.0])
constrains = np.array([[2.0, 1.0], [3.0, 1.0], [5.0, 1.0]])
ineq = np.array([80.0, 50.0, 70.0])

constrains_ = cvxopt.matrix(constrains)
ineq_ = cvxopt.matrix(ineq)
objective_ = cvxopt.matrix(obj_fun)

solution = cvxopt.solvers.lp(objective_, constrains_, ineq_)
print(solution)
print(np.array(solution['x']))
