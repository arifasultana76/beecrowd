def evaluate(x, y, op):
    return x + y if op == '+' else x - y if op == '-' else x * y


try:
    while True:
        T = int(input())
        expressions = []
        players = []

        for _ in range(T):
            x, yz = input().split()
            x = int(x)
            y, z = map(int, yz.split('='))
            expressions.append((x, y, z))

        for _ in range(T):
            name, e, r = input().split()
            e = int(e) - 1
            players.append((name, e, r))

        losers = []

        for name, e, r in players:
            x, y, z = expressions[e]
            correct = (
                (r == '+' and evaluate(x, y, '+') == z) or
                (r == '-' and evaluate(x, y, '-') == z) or
                (r == '*' and evaluate(x, y, '*') == z) or
                (r == 'I' and all(evaluate(x, y, op) != z for op in '+-*'))
            )
            if not correct:
                losers.append(name)

        if len(losers) == 0:
            print('You Shall All Pass!')
        elif len(losers) == T:
            print('None Shall Pass!')
        else:
            print(' '.join(sorted(losers)))

except EOFError:
    pass
