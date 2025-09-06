n = int(input().strip())

# Initialise counters
hobbits = humanos = elfos = anoes = magos = 0

# Process each person
for r in range(n):
    name, race = input().split()
    if race == 'X':
        hobbits += 1
    elif race == 'H':
        humanos += 1
    elif race == 'E':
        elfos += 1
    elif race == 'A':
        anoes += 1
    elif race == 'M':
        magos += 1

# Output in required order (Portuguese)
print(f"{hobbits} Hobbit(s)")
print(f"{humanos} Humano(s)")
print(f"{elfos} Elfo(s)")
print(f"{anoes} Anao(oes)")
print(f"{magos} Mago(s)")
