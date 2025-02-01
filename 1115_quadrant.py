while True:
    x,y = map(int,input().split())

    if (x == 0) or (y == 0):
        break
    if (x > 0) and (y > 0):
        print(f"primeiro")
    if (x < 0) and (y > 0):
        print(f"segundo")
    if (x < 0) and (y < 0):
        print(f"terceiro")
    if (x > 0) and (y < 0):
        print(f"quarto")
