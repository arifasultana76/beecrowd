import math

n = int(input().strip())

ships = [tuple(map(int, input().split())) for i in range(n)]

for i in range(n):
    min_dist = float('inf')
    for j in range(n):
        if i != j:

            d = math.sqrt(
                (ships[i][0] - ships[j][0])**2 +
                (ships[i][1] - ships[j][1])**2 +
                (ships[i][2] - ships[j][2])**2
            )
            if d < min_dist:
                min_dist = d

    if min_dist <= 20:
        print("A")
    elif min_dist <= 50:
        print("M")
    else:
        print("B")
