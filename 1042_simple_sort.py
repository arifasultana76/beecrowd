val = list(map(int,input().split()))
val2 = val.copy()
val.sort()

for i in range(len(val)):
    print(val[i])

print()

for j in range(len(val2)):
    print(val2[j])