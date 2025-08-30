import math


def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


# Input
N = int(input())
A = list(map(int, input().split()))

maxA = max(A)

# Host candidate must be > maxA
candidate = maxA + 1
while True:
    if phi(candidate) == N:
        # check all numbers in A are coprime with candidate
        if all(math.gcd(candidate, x) == 1 for x in A):
            print(candidate)
            break
    candidate += 1
