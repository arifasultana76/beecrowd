def decode(code):
    groups = code.strip().split()
    dots = len(groups[0])
    groups_count = len(groups)
    index = (dots - 1) + 3 * (groups_count - 1)
    return chr(ord('a') + index)


try:
    while True:
        n = int(input())
        for _ in range(n):
            code = input().strip()
            print(decode(code))  # print each letter on its own line
except EOFError:
    pass
