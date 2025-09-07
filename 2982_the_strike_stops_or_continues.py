import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()
it = iter(data)
n = int(next(it))
expenses = funds = 0

for r in range(n):
    t = next(it).upper()
    c = int(next(it))
    if t == 'G':
        expenses += c
    else:
        funds += c

if funds >= expenses:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
