def kth_fibonot(K):
    fib = [1, 1]
    while fib[-1] <= 2*K+10:
        fib.append(fib[-1] + fib[-2])
    fib = set(fib)

    count = 0
    n = 1
    while True:
        if n not in fib:
            count += 1
            if count == K:
                return n
        n += 1


K = int(input())
print(kth_fibonot(K))
