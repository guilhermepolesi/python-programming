# Your task is to complete the code to evaluate the following expression:
# 3x**3 - 2x**2 + 3x - 1
# The result must be assigned to y.
# Remember that classical algebraic notation likes to omit the multiplication operator
# you need to use it explicitly. Notice how we changed the data type to ensure that x is a float.

x = 0
x = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
x = float(x)
y = x
print("y =", y)

x = 1
x = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
x = float(x)
y = x
print("y =", y)

x = -1
x = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
x = float(x)
y = x
print("y =", y)