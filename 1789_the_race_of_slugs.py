while True:
    try:
        l = int(input())
        speeds = list(map(int, input().split()))
        max_speed = max(speeds)
        print(1 if max_speed < 10 else 2 if max_speed < 20 else 3)
    except EOFError:
        break
