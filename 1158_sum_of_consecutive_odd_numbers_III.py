n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    odd_num = []
    count = 0

    while (count<y):
        if x % 2 != 0:
            odd_num.append(x)
            count += 1
        x += 1
    result = sum(odd_num)
    print(result)

