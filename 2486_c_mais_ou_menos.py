
vitamin_c = {
    'suco de laranja': 120, 'morango fresco': 85, 'mamao': 85,
    'goiaba vermelha': 70, 'manga': 56, 'laranja': 50, 'brocolis': 34
}

while (T := int(input())) != 0:
    total = sum(int(n) * vitamin_c[food] for _ in range(T)
                for n, food in [input().split(maxsplit=1)])
    print(f'Menos {total - 130} mg' if total >
          130 else f'Mais {110 - total} mg' if total < 110 else f'{total} mg')
