n = int(input())
k = int(input())
scores = [int(input()) for r in range(n)]

scores.sort(reverse=True)
threshold = scores[k - 1]

qualified = sum(1 for score in scores if score >= threshold)
print(qualified)
