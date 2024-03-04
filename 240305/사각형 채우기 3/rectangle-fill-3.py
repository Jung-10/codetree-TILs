n = int(input())
mod = 1000000007

dp = [0] * 1001
dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(4, n + 1) :
    dp[i] = (dp[i - 1] * 4) - (dp[i - 2] * 3)

print(dp[n] % mod)