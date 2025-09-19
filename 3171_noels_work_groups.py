n = int(input().strip())

group_time = {
    "bonecos": 8,
    "arquitetos": 4,
    "musicos": 6,
    "desenhistas": 12
}

hours = {
    "bonecos": 0,
    "arquitetos": 0,
    "musicos": 0,
    "desenhistas": 0
}

for r in range(n):
    name, group, h = input().split()
    h = int(h)
    hours[group] += h

total_gifts = 0
for group in hours:
    total_gifts += hours[group] // group_time[group]

print(total_gifts)
