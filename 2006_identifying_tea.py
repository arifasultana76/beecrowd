t = int(input())

# Read contestants' answers
answers = list(map(int, input().split()))

# Count how many answers match the correct tea type
correct_count = answers.count(t)

# Print the result
print(correct_count)
