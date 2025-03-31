while True:

    n = int(input())

    if n == 0:
        break

    matrix = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        matrix.append(row)

    for r in range(n):
        for c in range(n):
            matrix[r][c] = 2**(r+c)

    T = len(str(matrix[n-1][n-1]))
    for r in range(n):
        for c in range(n):
            matrix[r][c] = str(matrix[r][c])
            while len(matrix[r][c]) < T:
                matrix[r][c] = " "+matrix[r][c]

        m = " ".join(matrix[r])

        print(m)
    print()
