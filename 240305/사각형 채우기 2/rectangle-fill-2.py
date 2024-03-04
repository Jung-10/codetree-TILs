n = int(input())
mod = 10007

dp = [0] * 1001
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]
    for j in range(i - 3, -1, -1) :
        dp[i] = dp[i] + dp[j] * 2

print(dp[n] % mod)