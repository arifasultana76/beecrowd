x, y = map(int,input().split())  # x means product code, y means quantity

price = [0, 4.00, 4.50, 5.00, 2.00, 1.50]  # index will be count 0

bill = price[x]*y

print(f"Total: R$ {bill:.2f}")

