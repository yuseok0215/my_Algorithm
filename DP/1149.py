n = int(input())

p = []
for _ in range(n):
    p.append(list(map(int, input().split())))


dp = [0] * 1001

dp[i]  = p[i-1][]