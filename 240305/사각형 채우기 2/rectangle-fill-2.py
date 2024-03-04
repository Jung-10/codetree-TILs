n = int(input())
mod = 10007

dp = [0] * 1001
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]
    for j in range(i - 3, -1, -1) :
        dp[i] = dp[i] + 2 * dp[j]

print(dp[n] % mod)