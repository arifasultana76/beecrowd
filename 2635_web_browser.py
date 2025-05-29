try:
    while True:
        n = int(input())
        words = [input().strip() for r in range(n)]
        q = int(input())
        for r in range(q):
            prefix = input().strip()
            matches = [w for w in words if w.startswith(prefix)]
            if matches:
                print(len(matches), max(len(w) for w in matches))
            else:
                print(-1)
except EOFError:
    pass
