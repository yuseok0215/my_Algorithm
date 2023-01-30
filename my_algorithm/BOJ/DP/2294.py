import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]

dp = [10001] * (k+1)
dp[0] = 0

for i in coins:
    for j in range(i, k+1):
        dp[i] = min(dp[j], dp[j-i]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])