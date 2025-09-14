t = int(input().strip())

for r in range(t):

    john_score = 0
    for r in range(3):
        x, d = map(int, input().split())
        john_score += x * d

    mary_score = 0
    for r in range(3):
        x, d = map(int, input().split())
        mary_score += x * d
    if john_score > mary_score:
        print("JOAO")
    else:
        print("MARIA")
