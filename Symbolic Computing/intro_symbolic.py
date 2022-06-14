import sympy
import numpy as np

#                                                    Defining a variable
# The name of a Symbol object is set when it is created. Symbols can be created in a few different ways in SymPy,
# for example, using sympy.Symbol, sympy.symbols, and sympy.var.

x = sympy.Symbol("x")
y, z = sympy.symbols("y, z")  # --> easiest way to define all the symbols used in an exercise
w = sympy.var("a")

print(f"The symbols defined are {x}, {y}, {z}, {w}")

# Symbols must be further defined:
# Assumption                                        Keyword Arguments
# real, imaginary                                   is_real, is_imaginary
# positive, negative                                is_positive, is_negative
# integer                                           is_integer
# odd, even                                         is_odd, is_even
# prime                                             is_prime
# finite, infinite                                  is_finite, is_infinite

x1 = sympy.Symbol("x1", positive=True, finite=True, even=True)
y1 = sympy.Symbol("y1")

print(sympy.sqrt(x1 ** 2))  # Has information, simplifies the expression
print(sympy.sqrt(y1 ** 2))

n = sympy.Symbol("n", integer=True, odd=True)
print(sympy.cos(n * sympy.pi))

print()

# Functions

f = sympy.Function("f")
print(f(x))

# Lambda functions
l_fun = sympy.Lambda(x, x ** 2)
print(l_fun(1 - x))
print(l_fun(5))

print()
print()

# ----------------------------------------------------------------------------------------------------------------------
# Expressions
# Function                        Description
# sympy.simplify                  Attempt various methods and approaches to obtain a simpler form of a given expression.
# sympy.trigsimp                  Attempt to simplify an expression using trigonometric identities.
# sympy.powsimp                   Attempt to simplify an expression using laws of powers.
# sympy.compsimp                  Simplify combinatorial expressions.
# sympy.ratsimp                   Simplify an expression by writing on a common denominator.
# sympy.factor                    Factors the expression
# sympy.expand                    Expands the expression
# expression.collect              Collects a certain variable

expr = sympy.exp(x) * sympy.exp(y)
print(expr)
print(sympy.simplify(expr))

expr2 = (x + 1) * (x + 2)
print(expr2)
print(sympy.expand(expr2))

fac = sympy.factor(x ** 2 - 1)
print(fac)

expr3 = x + y * x * z - 2 * x * z + x * z - y * z
print(expr3.collect(x))

print()

# Apart, Together and cancel
expr4 = 1 / (x ** 2 + 3 * x + 2)
print(sympy.apart(expr4, x))

expr5 = 1 / (y * x + y) + 1 / (1 + x)
print(sympy.together(expr5))

expr6 = y / (y * x + y)
print(sympy.cancel(expr6, y))

print()
print()

# ---------------------------------------------------------------------------------------------------------------------
#                                               Substitutions
# In the most basic use of subs, the method is called in an expression, and the symbol or expression that is to be
# replaced (x) is given as the first argument, and the new symbol or the expression (y) is given as the second argument.

a = x + y
a_sub = a.subs(x, y)
print(a_sub)

# Instead of chaining multiple subs calls when multiple substitutions are required, we can alternatively pass a
# dictionary as the first and only argument to subs that maps old symbols or expressions to new symbols or expressions:

b = sympy.sin(x * z)
b_sub = b.subs({x: y ** 2, z: sympy.exp(y), sympy.sin: sympy.log})
print(b_sub)

c = x * y + z ** 2 * x
values = {x: 1.25, y: 0.4, z: 3.2}
c_evalueted = c.subs(values).evalf(
    4)  # .evalf specifies the number of significant digits to which the expression is to be evaluated

print(c_evalueted)

print()

# Evaluating over a range of values
d = sympy.sin(sympy.pi * x * sympy.exp(x))
d_expre = sympy.lambdify(x, d, "numpy")

vals = np.arange(0, 10)
print(d_expre(vals))
