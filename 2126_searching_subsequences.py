case = 1
try:
    while True:
        n1 = input().strip()
        n2 = input().strip()

        count = 0
        last_pos = -1
        for i in range(len(n2) - len(n1) + 1):
            if n2[i:i+len(n1)] == n1:
                count += 1
                last_pos = i + 1  # 1-based index

        print(f"Caso #{case}:")
        if count:
            print(f"Qtd.Subsequencias: {count}")
            print(f"Pos: {last_pos}\n")
        else:
            print("Nao existe subsequencia\n")

        case += 1
except EOFError:
    pass
