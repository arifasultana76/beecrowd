def knight_move(start, end):
    col_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    # Convert chess notation to coordinates
    x1, y1 = col_map[start[0]], int(start[1])
    x2, y2 = col_map[end[0]], int(end[1])

    dx, dy = abs(x1 - x2), abs(y1 - y2)

    if (dx, dy) in [(1, 2), (2, 1)]:
        return "VALIDO"
    else:
        return "INVALIDO"


# Input
start, end = input().split()
print(knight_move(start, end))
