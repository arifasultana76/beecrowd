N = int(input().strip())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0] = A[0][:]  # row 1 has exactly one box

for i in range(1, N):                 # row i needs i+1 consecutive boxes
    for j in range(N - i):             # valid start positions
        row_sum = sum(A[i][j:j+i+1])
        dp[i][j] = row_sum + min(dp[i-1][j], dp[i-1][j+1])

print(dp[N-1][0])
