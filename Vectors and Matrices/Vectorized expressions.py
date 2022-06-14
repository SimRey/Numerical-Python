import numpy as np

# Arithmetic operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print()

# Useful function to collapse all values of an array into a value

tot_sum = np.add.reduce(np.arange(1, 6))
tot_mult = np.multiply.reduce(np.arange(1, 6))
print(tot_sum, tot_mult)

# Broadcasting

a = np.array([0, 1, 2])
b = np.ones((3, 3))
print(b + a)

c = np.array([0, 1, 2])[:, np.newaxis]
print(c + a)

# Broadcasting works similar to matrix multiplication, mxn and nxm must be consistent

print()
print()

# ---------------------------------------------------------------------------------------------------------------------
#                                               Aggregate functions
# NumPy provides another set of functions for calculating aggregates for NumPy arrays, which take an array as input and
# by default return a scalar as output. For example, statistics such as averages, standard deviations, and variances
# of the values in the input array, and functions for calculating the sum and the product of elements in an array,
# are all aggregate functions.

data = np.arange(1, 10).reshape(3, 3)
print(data)
print(data.sum())
print(data.sum(axis=0))  # Sum of each column
print(data.sum(axis=1))  # Sum of each line
# Same type of behaviour occurs with the other functions

print()
print()

x = np.linspace(-4, 4, 9)
alfa = np.where(x < 0, x ** 2, x ** 3)  # Chooses values from two arrays depending on the value of a condition array.
print(alfa)

beta = np.select([x < -1, x < 2, x >= 2],
                 [x ** 2, x ** 3, x ** 4])  # Chooses values from a list of arrays depending on a list of conditions.
print(beta)
gamma = np.choose([0, 0, 0, 1, 1, 1, 2, 2, 2], [x ** 2, x ** 3,
                                                x ** 4])  # Chooses values from a list of arrays depending on the
# values of a given index array.
print(gamma)

print()
print()


# Functions
def is_single(x):
    if x % 2 == 0:
        return True
    else:
        return False


is_even = np.vectorize(is_single)
vec = np.array([1, 2, 3, 4])
print(is_even(vec))

print()

fun = lambda x, y, z: x * 2 + y * 34 - z
ve = np.fromfunction(fun, (8, 4, 2))
print(ve)
print()

with open('file.txt', 'w') as file:
    matrix = """1,2,3
4,5,6 """
    print(matrix, file=file)

print(np.random.random((2, 3)))

np_text = np.genfromtxt('file.txt', delimiter=',')
print(np_text)

print()
print()

# ----------------------------------------------------------------------------------------------------------------
#                                               Matrix operations

m1 = np.array(([1, 2], [4, 5]))
m2 = np.array(([11, 12], [14, 15]))

dot_product = np.dot(m1, m2)
print(dot_product)

kron_delta = np.kron(m1, m2)
print(kron_delta)

print()
print()

# ---------------------------------------------------------------------------------------------------------------------
#                                                 Sorting
a = np.array([2, 1, 4, 3, 5])
b = a.copy()
a_sorted = a.sort()
a_indexes_sorted = np.argsort(b)
print(a)
print(a_indexes_sorted)

print()

# Sorting rows and columns
mat = np.random.randint(100, size=(3, 5))
mat2 = mat.copy()
colu_sort = np.sort(mat, axis=0)
line_sort = np.sort(mat2, axis=1)
print(mat)
print(colu_sort)
print(line_sort)

print()
print()

# --------------------------------------------------------------------------------------------------------------------
#                                                       Where

r_vals = np.random.random(5)
print(r_vals)

clause = np.where(r_vals < 0.5, "Less", "Bigger")
zipped = zip(r_vals, clause)
print(dict(zipped))
