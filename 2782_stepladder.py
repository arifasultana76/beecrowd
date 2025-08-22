def count_stepladders(seq):
    n = len(seq)
    if n <= 2:
        return 1  # Any 1 or 2 numbers form a single stepladder

    count = 1  # At least one stepladder exists
    diff = seq[1] - seq[0]

    for i in range(2, n):
        new_diff = seq[i] - seq[i-1]
        if new_diff != diff:
            count += 1
            diff = new_diff  # start a new ladder

    return count


n = int(input())
seq = list(map(int, input().split()))
print(count_stepladders(seq))
