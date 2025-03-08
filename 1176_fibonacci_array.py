t = int(input())

for i in range(t):

    n = int(input())
    sequence = [0, 1]

    for j in range(n):

        result = sequence[-1] + sequence[-2]
        sequence.append(result)

    print(f"Fib({n}) = {sequence[n]}")
