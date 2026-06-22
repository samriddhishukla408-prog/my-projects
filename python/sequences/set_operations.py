set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Difference (B - A):", set_b - set_a)
print("Symmetric Difference:", set_a ^ set_b)
set_a.add(10)
print("After adding 10 to Set A:", set_a)
set_a.discard(10)
print("After discarding 10:", set_a) 
print("Is A a subset of B?", set_a.issubset(set_b))
