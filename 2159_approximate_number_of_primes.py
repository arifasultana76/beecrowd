import math

n = int(input())

ln_n = math.log(n)

p = n / ln_n
m = 1.25506 * (n / ln_n)

print(f"{p:.1f} {m:.1f}")
