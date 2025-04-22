case_number = 1

while True:
    try:
        n = int(input())

        sequence = []
        for i in range(n + 1):
            sequence += [i] * i if i > 0 else [0]

        total = len(sequence)
        if total == 1:
            print(f"Caso {case_number}: {total} numero")
        else:
            print(f"Caso {case_number}: {total} numeros")

        print(' '.join(map(str, sequence)))
        print()

        case_number += 1

    except EOFError:
        break
