p, n = map(int, input().split())
heights = list(map(int, input().split()))

for i in range(1, n):
    if abs(heights[i] - heights[i - 1]) > p:
        print("GAME OVER")
        break
else:
    print("YOU WIN")
