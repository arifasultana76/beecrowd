pi = 3.14

while True:
    try:

        V = float(input())
        D = float(input())

        # Calculate radius and area of the mouth
        R = D / 2
        area = pi * (R ** 2)

        # Calculate height using volume formula: V = area × height
        height = V / area

        # Print results with 2 decimal places
        print(f"ALTURA = {height:.2f}")
        print(f"AREA = {area:.2f}")
    except EOFError:
        break
