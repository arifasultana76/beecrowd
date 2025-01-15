count = 0
p_num =[]
for i in range(6):
    num = float(input())

    if num > 0:
        count += 1

        p_num.append(num)

avg = sum(p_num)/count

print(f"{count} valores positivos")
print(f"{avg:.1f}")
