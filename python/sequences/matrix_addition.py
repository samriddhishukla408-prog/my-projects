matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]
 
matrix_b = [
    [7, 8, 9],
    [10, 11, 12]
]
 
rows = len(matrix_a)
cols = len(matrix_a[0])
 
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)
 
print("Matrix A:", matrix_a)
print("Matrix B:", matrix_b)
print("Sum of matrices:")
for row in result:
    print(row)
 