n = int(input())

p = [0] * (10001)
for i in range(1,n+1):
    p[i] = int(input())

dp = [0] * (10001)

dp[1] = p[1]
dp[2] = p[1] + p[2]
dp[3] = max(p[1]+p[3], p[2]+p[3])

for i in range(4,n+1):
    dp[i] = max(dp[i-1], p[i] + dp[i-2], p[i] + p[i-1] + dp[i-3])


print(dp[n])