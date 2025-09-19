import sys


def solve():
    inside = False
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line.strip() == "<body>":
            inside = True
            continue
        if line.strip() == "</body>":
            inside = False
            continue
        if inside:
            print(line)


if __name__ == "__main__":
    solve()
