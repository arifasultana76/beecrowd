import sys

for line in sys.stdin:
    if not line.strip():
        continue
    cpf = line.strip()
    # Split by '.' then '-'
    parts = cpf.replace("-", ".").split(".")
    for p in parts:
        print(p)
