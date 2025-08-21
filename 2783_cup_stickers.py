n, c, m = map(int, input().split())

# Stamped stickers (special ones)
stamped = set(map(int, input().split()))

# Purchased stickers
purchased = set(map(int, input().split()))

# Find how many stamped ones are already collected
collected_stamped = stamped & purchased

# Missing stamped stickers
missing = len(stamped) - len(collected_stamped)

print(missing)
