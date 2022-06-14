import sympy

#                                                       Equations
# Equation solving is a fundamental part of mathematics with applications in nearly every branch of science and
# technology, and it is therefore immensely important. SymPy can solve a wide variety of equations symbolically,
# although many equations cannot be solved analytically even in principle. If an equation, or a system of equations,
# can be solved analytically, there is a good chance that SymPy is able to find the solution. If not, numerical methods
# might be the only option

x, y = sympy.symbols("x, y")
eqn = x ** 2 + 2 * x - 3
roots = sympy.solve(eqn, dict=True)  # Specifying dict=True, displays the results as a dictionary
print(roots)
print()

# Direct solving
print(sympy.solve(sympy.exp(x) + 2 * x, x))
print()

# System of equations
eq1 = x + 2 * y - 1
eq2 = x - y + 1

sols = sympy.solve([eq1, eq2], [x, y], dict=True)
print(sols)

# Validation of the obtained results

for sol in sols:
    if eq1.subs(sol).simplify() == 0 and eq2.subs(sol).simplify() == 0:
        print(True)
    else:
        print(False)
