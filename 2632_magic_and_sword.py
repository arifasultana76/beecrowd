def intersects_circle_rectangle(rx, ry, w, h, cx, cy, r):

    closest_x = max(rx, min(cx, rx + w))
    closest_y = max(ry, min(cy, ry + h))

    dx = closest_x - cx
    dy = closest_y - cy

    return dx*dx + dy*dy <= r*r


spell_data = {
    'fire':  {'damage': 200, 'radius': [20, 30, 50]},
    'water': {'damage': 300, 'radius': [10, 25, 40]},
    'earth': {'damage': 400, 'radius': [25, 55, 70]},
    'air':   {'damage': 100, 'radius': [18, 38, 60]},
}

t = int(input())
for r in range(t):
    w, h, x0, y0 = map(int, input().split())
    spell, level, cx, cy = input().split()
    level = int(level)
    cx = int(cx)
    cy = int(cy)

    radius = spell_data[spell]['radius'][level - 1]
    damage = spell_data[spell]['damage']

    if intersects_circle_rectangle(x0, y0, w, h, cx, cy, radius):
        print(damage)
    else:
        print(0)
