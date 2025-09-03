n = int(input())
votes = [int(input()) for r in range(n)]

print("S" if votes[0] >= max(votes) else "N")
