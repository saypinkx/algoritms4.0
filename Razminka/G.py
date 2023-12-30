matrix = []
n, m = list(map(lambda x: int(x), str(input()).split()))
matrix.append([0]*(m+1))
for i in range(n):
    mass = list(map(lambda x: int(x), str(input()).split()))
    matrix.append([])
    matrix[i+1].append(0)
    matrix[i+1].extend(mass)
maximum = 0

for i in range(n+1):
    for j in range(m+1):
        if matrix[i][j] != 0:
            # matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
            deps = [(i - 1, j - 1), (i - 1, j), (i, j - 1)]
            dp_matrix = []
            for dep in deps:
                if dep[0] >= 0 and dep[1] >= 0:
                    dp_matrix.append(matrix[dep[0]][dep[1]])

            if len(dp_matrix) > 0:
                matrix[i][j] = min(dp_matrix) + 1

            # else:
            #     matrix[i][j] = 0
            if matrix[i][j] > maximum:
                if i != 0:
                    maximum = matrix[i][j]
        else:
            matrix[i][j] = 0

print(maximum)
for mass in matrix:
    print(mass)
