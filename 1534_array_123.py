while True:

    try:

        n = int(input())

        if 3 <= n <= 70:

            matrix = []

            for r in range(n):
                row = []
                for c in range(n):
                    row.append(3)
                matrix.append(row)

            for r in range(n):
                matrix[r][r] = 1
                matrix[r][n-1-r] = 2

            for r in range(n):
                for c in range(n):
                    print(matrix[r][c], end="")
                print()

    except EOFError:
        break
