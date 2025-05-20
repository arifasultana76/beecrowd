import sys

while True:
    try:
        m = int(input())
        total_weighted_score = total_credits = 0
        for _ in range(m):
            ni, ci = map(int, input().split())
            total_weighted_score += ni * ci
            total_credits += ci
        api = total_weighted_score / (total_credits * 100)
        print(f'{api:.4f}')
    except EOFError:
        break
