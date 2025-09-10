n = int(input().strip())

cars = 0
dolls = 0

for r in range(n):
    name, gender = input().split()
    if gender == 'M':
        cars += 1
    elif gender == 'F':
        dolls += 1

# Output result
print(f"{cars} carrinhos")
print(f"{dolls} bonecas")
