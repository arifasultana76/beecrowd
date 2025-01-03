n = int(input())

hrs = n // 3600
min = (n % 3600) // 60
sec = n % 60

print(f"{hrs}:{min}:{sec}")