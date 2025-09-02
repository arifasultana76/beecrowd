# Read the five integers (each on its own line or space-separated)
parts = [int(input()) for r in range(5)]

# Portion sizes in grams
sizes = [300, 1500, 600, 1000, 150]

# Calculate total for the guests
total = sum(p * s for p, s in zip(parts, sizes))

# Add Dona Chica's portion
total += 225

print(total)
