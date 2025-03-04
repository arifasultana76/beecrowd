n = int(input())

for i in range(n):

    x = int(input())
    divisor = []

    for j in range(1,x):
        if x % j == 0:
            divisor.append(j)

    if sum(divisor) == x:
        print(f"{x} eh perfeito")

    else:
        print(f"{x} nao eh perfeito")