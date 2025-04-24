n = int(input())
numbers = list(map(int, input().split()))

count_2 = count_3 = count_4 = count_5 = 0

for num in numbers:
    if num % 2 == 0:
        count_2 += 1
    if num % 3 == 0:
        count_3 += 1
    if num % 4 == 0:
        count_4 += 1
    if num % 5 == 0:
        count_5 += 1

print(f"{count_2} Multiplo(s) de 2")
print(f"{count_3} Multiplo(s) de 3")
print(f"{count_4} Multiplo(s) de 4")
print(f"{count_5} Multiplo(s) de 5")
