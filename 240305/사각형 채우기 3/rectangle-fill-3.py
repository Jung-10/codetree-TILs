n = int(input())
mod = 1000000007

dp = [0] * 1001
dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(4, n + 1) :
    dp[i] = (dp[i - 2] * (i - 1)) + (dp[i - 1] * i) - i

print(dp[n] % mod)