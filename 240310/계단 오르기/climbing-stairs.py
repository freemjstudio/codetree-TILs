n = int(input())
MAX = 1000
dp = [0] * (MAX+1)

dp[1] = 1
dp[2] = 1
dp[3] = 1
if n > 3:
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-3]

print(dp[n]%10007)