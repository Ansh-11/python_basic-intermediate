matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# printing the old matrix
for row in matrix:
    print(row)

# transforming the nre transpose
newmatrix = [[matrix[j][i]
              for j in range(len(matrix))]for i in range(len(matrix[0]))]
print("\n the transpose matrix is avilable")

# printiing the transpose matrix
for row in newmatrix:
    print(row)
