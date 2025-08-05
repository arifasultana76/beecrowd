# Read input and split into a list of integers
cups = list(map(int, input().split()))

# Find the index of the cup with the bean (value 1)
# +1 because cup numbers are 1-based
print(cups.index(1) + 1)
