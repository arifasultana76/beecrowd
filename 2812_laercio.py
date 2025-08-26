t = int(input().strip())  # number of test cases

for _ in range(t):
    m = int(input().strip())  # size of list
    nums = list(map(int, input().split()))

    # keep only odd numbers
    odds = [x for x in nums if x % 2 == 1]

    # sort ascending
    odds.sort()

    result = []
    i, j = len(odds) - 1, 0
    toggle = True  # start with largest

    while j <= i:
        if toggle:
            result.append(odds[i])  # largest
            i -= 1
        else:
            result.append(odds[j])  # smallest
            j += 1
        toggle = not toggle

    print(" ".join(map(str, result)))
