
import sys


def solve():
    input_lines = sys.stdin.read().split()
    idx = 0
    results = []

    while idx < len(input_lines):
        N = int(input_lines[idx])
        idx += 1

        e1, e2 = int(input_lines[idx]), int(input_lines[idx+1])
        idx += 2

        a1 = list(map(int, input_lines[idx:idx+N]))
        idx += N

        a2 = list(map(int, input_lines[idx:idx+N]))
        idx += N

        t1 = list(map(int, input_lines[idx:idx+N-1]))
        idx += N - 1

        t2 = list(map(int, input_lines[idx:idx+N-1]))
        idx += N - 1

        x1, x2 = int(input_lines[idx]), int(input_lines[idx+1])
        idx += 2

        # DP arrays
        T1 = [0]*N
        T2 = [0]*N

        T1[0] = e1 + a1[0]
        T2[0] = e2 + a2[0]

        for i in range(1, N):
            T1[i] = min(T1[i-1] + a1[i], T2[i-1] + t2[i-1] + a1[i])
            T2[i] = min(T2[i-1] + a2[i], T1[i-1] + t1[i-1] + a2[i])

        result = min(T1[N-1] + x1, T2[N-1] + x2)
        results.append(str(result))

    print("\n".join(results))


solve()
