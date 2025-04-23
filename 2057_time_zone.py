s, t, f = map(int, input().split())

arrival = (s + t + f) % 24
print(arrival)
