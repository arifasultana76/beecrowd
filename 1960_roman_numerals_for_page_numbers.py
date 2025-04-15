num = int(input())

val = [900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
sym = ["CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

result = ""
for i in range(len(val)):
    result += sym[i] * (num // val[i])
    num %= val[i]

print(result)
