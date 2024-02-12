def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = [[float(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]


print("Original Matrix:")
for row in matrix:
    print(row)


transposed_matrix = transpose(matrix)
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
