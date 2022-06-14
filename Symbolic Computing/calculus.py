import sympy

# Derivatives
x, y, z, a, b = sympy.symbols("x, y, z, a, b")

f = sympy.Function("f")
g = sympy.Function("g")
f = f(x)
g = g(x, y)

# Total differential
df = f.diff(x)  # when placing x, # the order of the differential is specified
print(df)
# Another way to define a differential is by writing sympy.Derivative(function, variable, order)
df2 = sympy.Derivative(f, x)
print(df2)

# Partial differential
dg = g.diff(x, 2, y, 4)
print(dg)

# Solving a derivative
ex = x ** 4 + x ** 3 + x ** 2 + x + 1
print(ex.diff(x))

expr = (x + 1) ** 3 * y ** 2 * (z - 1)
print(expr.diff(x, y, z))  # Order of variables indicates the order of derivation

print()
print()

# ----------------------------------------------------------------------------------------------------------------------
#                                               Integrals

# Non-defined integral
f_non = sympy.integrate(f)
print(f_non)
f_non2 = sympy.Integral(f, x)
print(f_non2)

# Defined integral
f_def = sympy.integrate(f, (x, a, b))
print(f_def)

# Solving integrals
ex1 = sympy.exp(-x ** 2)
int_ex1 = sympy.integrate(ex1, (x, 0, sympy.oo))
print(int_ex1)

print()

# Multivariable integrals
ex2 = (x + y)**2
print(ex2)
int_ex21 = sympy.integrate(ex2, x)
print(int_ex21)
int_ex22 = sympy.integrate(ex2, y)
print(int_ex22)
int_ex23 = sympy.integrate(ex2, x, y)
print(int_ex23)
int_ex23_eval = sympy.integrate(ex2, (x, 0, 1), (y, 0, 1))
print(int_ex23_eval)

print()
print()

# ---------------------------------------------------------------------------------------------------------------------
#                                                Series
series_f = sympy.series(f, x)
print(series_f)

# To change the point around which the function is expanded, we specify the x0 argument as in the following example:
x0 = sympy.Symbol("{x_0}")
print(f.series(x, x0, n=2))
# Here we also specified n=2, to request a series expansion with only terms up to and including the second order.

print()

# Solving series

cos_series = sympy.cos(x).series()
print(cos_series)
sin_series = sympy.sin(x).series()
print(sin_series)
exp_series = sympy.exp(x).series()
print(exp_series)
alpha = (1/(1+x)).series()
print(alpha)

print()
print()

# ---------------------------------------------------------------------------------------------------------------------
#                                                Sums and Products
n = sympy.symbols("n", integer=True)
n_sum = sympy.Sum(1/(n**2), (n, 1, sympy.oo))
print(n_sum)
print(n_sum.doit())

n_prod = sympy.Product(n, (n, 1, 7))
print(n_prod)
print(n_prod.doit())

print()
print()

# ---------------------------------------------------------------------------------------------------------------------
#                                                Limits
lim = sympy.limit(f, x, sympy.oo)
print(lim)

sin_lim = sympy.limit(sympy.sin(x) / x, x, 0)
print(sin_lim)