x = int(input())
odd = []
if x >= 1 and x <= 1000:

    for i in range(x+1):
        if i % 2 != 0:
            odd.append(i)
for i in odd:
    print(i)