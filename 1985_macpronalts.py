menu = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

p = int(input())

total = 0.0

# Loop through each product purchase
for _ in range(p):
    code, quantity = map(int, input().split())
    if code in menu:
        total += menu[code] * quantity

# Print total with 2 decimal places
print(f"{total:.2f}")
