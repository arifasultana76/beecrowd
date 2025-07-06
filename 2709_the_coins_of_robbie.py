import sys


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


input_lines = sys.stdin.read().splitlines()
i = 0

while i < len(input_lines):
    m = int(input_lines[i])
    i += 1
    coins = []
    for r in range(m):
        coins.append(int(input_lines[i]))
        i += 1
    n = int(input_lines[i])
    i += 1

    selected = coins[::-1][::n]
    total = sum(selected)

    if is_prime(total):
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else:
        print("Bad boy! I’ll hit you.")
