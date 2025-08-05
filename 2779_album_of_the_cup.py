# Input
n = int(input())              # Total number of unique cards
m = int(input())              # Total purchased cards
purchased = set()             # Using a set to avoid duplicates

for r in range(m):
    purchased.add(int(input()))

# Output
print(n - len(purchased))
