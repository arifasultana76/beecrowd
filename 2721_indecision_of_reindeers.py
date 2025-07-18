# List of reindeer in order

reindeers = ['Dasher', 'Dancer', 'Prancer', 'Vixen',
             'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

# Read input: 9 integers representing the number of snowballs each reindeer made
snowballs = list(map(int, input().split()))

# Calculate the total number of snowballs
total_snowballs = sum(snowballs)

# The index of the reindeer who gets the last snowball
winner_index = (total_snowballs - 1) % 9

# Output the name of the winning reindeer
print(reindeers[winner_index])
