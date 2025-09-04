n, g = map(int, input().split())
val = {r: int(v) for _ in range(n) for r, v in [input().split()]}

x = int(input())
runes = input().split()  # works if runes are space-separated
if len(runes) == 1 and len(runes[0]) == x:  # handle unspaced runes
    runes = list(runes[0])

total = sum(val.get(r, 0) for r in runes)

print(total)
print("You shall pass!" if total >= g else "My precioooous")
