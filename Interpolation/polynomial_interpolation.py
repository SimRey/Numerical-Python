import numpy as np
import matplotlib.pyplot as plt
from numpy import polynomial as P

#                                           Polynomial interpolation
# Each of the polynomial classes in polynomial conveniently provides a function for computing the (generalized)
# Vandermonde matrix for the corresponding basis. Using the above mentioned functions for generating the Vandermonde
# matrices, we can easily perform a polynomial interpolation in different bases. For example, consider the data points
# (1, 1), (2, 3), (3, 5), and (4, 4).

x = np.array([1, 2, 3, 4])
y = np.array([1, 3, 5, 4])

deg = len(x) - 1
A = P.polynomial.polyvander(x, deg)
c = np.linalg.solve(A, y)
print(c)  # coefficients for a polynomial
f1 = P.Polynomial(c)  # adjusted polynomial

# While interpolation with different polynomial bases is convenient due to the functions for the generalized Vandermonde
# matrices, there is an even simpler and better method available. Each polynomial class provides a class method fit that
# can be used to compute an interpolation polynomial.

f1b = P.Polynomial.fit(x, y, 2)  # Degree can be played with (works like the polyvander), in this case warning arises
                                 # if degree > 3
print(f1b)

xx = np.linspace(min(x), max(x), 101)
fig, ax = plt.subplots()
ax.scatter(x, y, label="Scatter points")
ax.plot(x, f1(x), color="red", lw=2, label="Edgy polynomial")
ax.plot(xx, f1(xx), color="black", lw=2, label="Smooth polynomial")
ax.plot(xx, f1b(xx), color="yellow", lw=2, label="Fitted polynomial")
ax.legend(loc="best")
ax.grid()
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
