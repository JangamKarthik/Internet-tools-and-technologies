def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))

matrix1 = [[float(input(f"Enter element at position ({i+1}, {j+1}) for the first matrix: ")) for j in range(cols1)] for i in range(rows1)]

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

matrix2 = [[float(input(f"Enter element at position ({i+1}, {j+1}) for the second matrix: ")) for j in range(cols2)] for i in range(rows2)]

result_matrix = add_matrices(matrix1, matrix2)

print("Resultant Matrix:")
for row in result_matrix:
    print(row)
