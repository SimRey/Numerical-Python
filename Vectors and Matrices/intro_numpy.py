import numpy as np

# Basic operations

data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)
print()
print(type(data))
print(data.ndim)  # Dimension of the array
print(data.shape)  # Tuple with lines and columns

print()
print()
# ----------------------------------------------------------------------------------------------------------------------
# dtype: The data type of the elements in the array

array1 = np.array(([1, 2, 3], [4, 5, 6]), dtype=np.int)
array2 = np.array(([1, 2, 3], [4, 5, 6]), dtype=np.float)
array3 = np.array(([1, 2, 3], [4, 5, 6]), dtype=np.complex)
print(array1)
print(array2)
print(array3)

print()
print()
# ----------------------------------------------------------------------------------------------------------------------
#                                                 Creating arrays

a = np.array([1, 2, 3])  # Creates an array for which the elements are given by an array-like object, which,
# for example, can be a (nested) Python list, a tuple, an iterable sequence, or another ndarray instance.
print(a)
b = np.zeros((3, 3))  # Creates an array with the specified dimensions and data type that is filled with zeros. Similar
# it can be used np.ones(), which returns 1s instead of zeros.
print(b)
c = np.full((3, 3), 34)  # Array with a specific dimension filled with a constant
print(c)
d = np.empty((2, 3))
d.fill(8)
print(d)
e = np.identity(3)  # In this case a n-square identity-matrix is created
print(e)

print()
print()

# ----------------------------------------------------------------------------------------------------------------------
#                                               Special arrays
# Arrays Filled with Incremental Sequences
a1 = np.arange(0, 11, 2)  # Vector with starting value, end-1 value, step
print(a1)
b1 = np.linspace(0, 10, 6)  # Vector with starting value, end value, number of elements
print(b1)
c1 = np.logspace(0, 10, 10)  # 10 data points between 1e0 to 1e10
print(c1)
# Multidimensional coordinate grids can be generated using the function np.meshgrid. Given two one-dimensional
# coordinate arrays (i.e., arrays containing a set of coordinates along a given dimension), we can generate
# two-dimensional coordinate arrays using the np.meshgrid function.
x1 = np.array([-1, 0, 1])
y1 = np.array([-2, 0, 2])
X, Y = np.meshgrid(x1, y1)
print(X)  # 2D vector --> matrix 3x3
print(Y)  # 2D vector --> matrix 3x3

print()
print()

# ----------------------------------------------------------------------------------------------------------------
#                                          Slicing
matrix_34 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(matrix_34)
print(matrix_34[2, 0])
print(matrix_34[:2, 1:3])

print()
print()

# ----------------------------------------------------------------------------------------------------------------
#                                        Resize and Reshape

h1 = np.array([[1, 2], [3, 4]])
h11 = np.reshape(h1, (4, 1))  # Vector to be reshaped and structure
print(h11)
print()
h12 = h1.flatten()  # Makes a vector out of a matrix
print(h12)

h13 = h1.T  # Command to transpose a matrix
print(h13)
print()
h14 = np.resize(h1, (5, 5))  # Resizes an array. Creates a new copy of the original array, with the requested size.
# If necessary, the original array will be repeated to fill up the new array.
print(h14)
h15 = np.vstack((h1, h1))  # Stacks vertically arrays
print(h15)

print()
print()

# ----------------------------------------------------------------------------------------------------------------
#                                       Concatenating and splitting

i1 = np.array([[1, 2, 3], [4, 5, 6]])
i2 = np.array([[6, 5, 4], [3, 2, 1]])

# Two types of concatenations:
#       Underneath the first matrix --> axis = 0 (also .vstack())
concate1 = np.concatenate([i1, i2], axis=0)
print(concate1)
#       Besides the first matrix --> axis = 1 (also .hstack())
concate2 = np.concatenate([i1, i2], axis=1)
print(concate2)

print()

# Splitting
i3 = [1, 2, 3, 99, 99, 3, 2, 1]
i31, i32, i33 = np.split(i3, [3, 5])  # in .split() the first argument is the list, the second boundaries of splitting
print(i31, i32, i33)

# similar usage with .vsplit() and .hsplit(), where the first argument is a list and the second the boundires

print()
print()
# ---------------------------------------------------------------------------------------------------------------------
#                                       Transposing vectors

j = np.array([1, 2, 3, 4, 5, 6])
print(j)

j_trans = j[:, np.newaxis]
print(j_trans)

j_back = j[np.newaxis, :]
print(j_back)

# In this case the vector or matrix entered will increase its dimension to one value when using np.newaxis
