nested_list = [[1, 2], [3, 4], [5, 6, 7]]
flat_list = []
for element in nested_list:
    for i in element:
        flat_list.append(i)
print("Flattened (loop method):", flat_list)