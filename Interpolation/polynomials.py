import numpy as np
from numpy import polynomial as P

#                                                   Polynomials
# The np.polynomial module contains a number of classes for representing polynomials in different polynomial bases.
# Standard polynomials, written in the usual power basis {xi}, are represented with the Polynomial class. To create an
# instance of this class, we can pass a coefficient array to its constructor. In the coefficient array, the ith element
# is the coefficient of xi.

# Example: representation of the polynomial 1+2x+3x^2

p1 = P.Polynomial([1, 2, 3])
print(p1)  # --> should print: Polynomial([-1., 0., 1.], domain=[-1., 1.], window=[-1., 1.])
# To access each element:
print(p1.coef)
print(p1.domain)
print(p1.window)

print()

p2 = P.Polynomial.fromroots([-1, 1])  # Polynomial can be obtained form its roots
print(p2)
print()

# To calculate the roots of a polynomial use the method P.Polynomial.roots()
print(P.Polynomial.roots(p2))
print()

# Polynomial evaluation
p1_eval = p1(np.array([1, 1.5, 2]))  # Evaluated at 1, 1.5 and 2
print(p1_eval)
print()

# Instances of Polynomial can be operated on using the standard arithmetic operators +, -, *, /, and so on.
# The // operator is used for polynomial division.
# Ex:
P1 = P.Polynomial.fromroots([1, 2, 3])
P2 = P.Polynomial.fromroots([2])
P3 = P1//P2
print(P3)
print(P3.roots())
