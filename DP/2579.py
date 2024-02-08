n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

dp = [0] * (n+1)
dp[1] = score[0]
dp[2] = score[0] + score[1]


for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] - dp[i-3]

print(dp[n])
