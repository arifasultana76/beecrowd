n = int(input())

for r in range(n):

    name = input().strip()

    difficulty = float(input().strip())

    scores = list(map(float, input().strip().split()))

    scores.remove(max(scores))
    scores.remove(min(scores))

    final_score = sum(scores) * difficulty

    print(f"{name} {final_score:.2f}")
