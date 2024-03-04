n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1) :
    dp[i] = i + i-1

print(dp[i])