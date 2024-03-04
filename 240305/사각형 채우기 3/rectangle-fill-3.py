n = int(input())
mod = 1000000007

dp = [0] * 1001
dp[0] = 1 # 타일을 전혀 놓지 않는 경우가 한 가지 있으므로 의미상 1
dp[1] = 2

for i in range(2, n + 1) :
    dp[i] = (dp[i - 1] * 2) + (dp[i - 2] * 3)

    for j in range(i - 3, -1, -1) :
        dp[i] = (dp[i] + dp[j] * 2)

print(dp[n] % mod)