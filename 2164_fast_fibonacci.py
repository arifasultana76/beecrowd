import math

n = int(input())

phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2

fib_n = (phi**n - psi**n) / math.sqrt(5)

print(f"{fib_n:.1f}")
