val = float(input())

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")

for i in notes:
    quotiont = int(val / i)
    print(f'{quotiont} nota(s) de R$ {i:.2f}')
    remainder = val % i
    val = remainder

print("MOEDAS:")

for j in coins:
    quotiont = int(round(val,2) / j)
    print(f'{quotiont} moeda(s) de R$ {j:.2f}')
    remainder = val % j
    val = remainder