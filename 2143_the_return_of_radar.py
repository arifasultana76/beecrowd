# while True:
#     T = int(input())
#     if T == 0:
#         break

#     for r in range(T):
#         N = int(input())

#         orders = 2 * (N + 5)
#         print(orders)

while True:
    T = int(input())  
    if T == 0:
        break  

    results = []
    for _ in range(T):
        N = int(input())  
        orders = 2 * (N - 1)  
        results.append(str(orders))

    print(" ".join(results))
