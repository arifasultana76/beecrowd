a, b, c = map(int, input().split())
ok = 0
s = [a, b, c]

for i in [-1, 1]:
    if i*s[0] == 0 or i*s[1] == 0 or i*s[2] == 0:
        ok = 1
for i in [-1, 1]:
    for j in [-1, 1]:
        if i*s[0] + j*s[1] == 0 or i*s[0] + j*s[2] == 0 or i*s[1] + j*s[2] == 0:
            ok = 1
for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            if i*s[0] + j*s[1] + k*s[2] == 0:
                ok = 1

print('S' if ok else 'N')
