# Tuple creation
coordinates = (10, 20)
print("Tuple:", coordinates)
# Packing
point = 5, 10, 15
print("Packed tuple:", point)
# Unpacking
x, y, z = point
print("Unpacked values:", x, y, z)
# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))
print("Index of first 3:", numbers.index(3))
nested = (1, (2, 3), (4, 5))
print("Nested tuple:", nested)
print("Accessing nested value:", nested[1][0])