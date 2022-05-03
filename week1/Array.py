import numpy as np
import math
import linecache

# Arrays are displayed as a list or list of lists and can be created through list as well. When creating an
# array, we pass in a list as an argument in numpy array
a = np.array([[1, 2, 3], [4, 6, 7], [4, 6, 7]])
b = np.array([[3, 2, 1], [4, 6, 7], [4, 6, 7]])
e = np.ones((2, 3))
z = np.random.rand(2, 3)
k = np.arange(0, 21, 5)
x = np.linspace(0, 125, 5)
y = np.arange(1, 26, 1).reshape(5, 5)
print(np.array([a[0, 0], b[0, 0]]))
print(e>0)
print(a)
print(b)
# We can print the number of dimensions of a list using the ndim attribute
print(a.ndim)
print(b.ndim)
print(b.shape)  # (число даннх в одной ячайке матрицы, сколько всего ячеек
print(a.shape)  # (число даннх в одной ячайке матрицы, сколько всего ячеек
print(a.dtype)  # Тип данных
print(z)
print(a * b)
print(a.sum())
print(a.max())
print(a.min())
print(y)
