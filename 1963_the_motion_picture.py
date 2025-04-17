# Read input values
a, b = map(float, input().split())

# Calculate percentage increase
increase = ((b - a) / a) * 100

# Print the result with two decimal places followed by the percentage symbol
print(f"{increase:.2f}%")
