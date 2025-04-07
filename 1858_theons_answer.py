n = int(input())
t = list(map(int, input().split()))

min_hits = t[0]
person = 1

for i in range(1, n):
    if t[i] < min_hits:
        min_hits = t[i]
        person = i + 1

print(person)
