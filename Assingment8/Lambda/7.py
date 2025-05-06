matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

sorted_matrix1 = sorted(matrix1, key=lambda x: sum(x))
sorted_matrix2 = sorted(matrix2, key=lambda x: sum(x))

print(sorted_matrix1)
print(sorted_matrix2)
