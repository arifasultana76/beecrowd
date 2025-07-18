def main():
    import re

    def get_tokens(formula):
        return re.findall(r'[A-Z][a-z]*\d*', formula)

    n = int(input())
    for test_case in range(n):
        if test_case > 0:
            print()

        t = int(input())
        dangerous = [get_tokens(input().strip()) for r in range(t)]

        u = int(input())
        for r in range(u):
            experiment = get_tokens(input().strip())
            found = False
            for d in dangerous:
                for i in range(len(experiment) - len(d) + 1):
                    if experiment[i:i+len(d)] == d:
                        found = True
                        break
                if found:
                    break
            print("Abortar" if found else "Prossiga")


if __name__ == "__main__":
    main()
