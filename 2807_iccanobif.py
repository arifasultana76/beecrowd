n = int(input().strip())

if n == 1:
    print(1)
else:
    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    print(" ".join(map(str, fib[::-1])))
