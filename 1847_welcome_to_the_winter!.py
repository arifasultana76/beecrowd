A, B, C = map(int, input().split())

if B < A and C >= B:
    print(":)")
elif B > A and C <= B:
    print(":(")
elif B > A and C > B:
    if C - B >= B - A:
        print(":)")
    else:
        print(":(")
elif B < A and C < B:
    if B - C < A - B:
        print(":)")
    else:
        print(":(")
elif A == B:
    if C > B:
        print(":)")
    else:
        print(":(")
