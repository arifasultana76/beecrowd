while True:
    try:
        n = int(input())
        matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            matrix[i][i] = 2  # Main diagonal
            matrix[i][n - i - 1] = 3  # Secondary diagonal

        inner_start = n // 3
        inner_end = n - inner_start

        for i in range(inner_start, inner_end):
            for j in range(inner_start, inner_end):
                matrix[i][j] = 1  # Inner square

        matrix[n // 2][n // 2] = 4  # Central element

        for row in matrix:
            print("".join(map(str, row)))
        print()
    except EOFError:
        break
