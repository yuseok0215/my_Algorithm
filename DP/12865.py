import sys
input = sys.stdin.readline

n,k = map(int, input().split())
item = []

for _ in range(n):
    w,v = map(int, input().split())
    item.append((w,v))

dp = [0] * (k+1)


for weight, value in item:
    for i in range(k,weight-1, -1):
        dp[i] = max(dp[i-weight] + value , dp[i])        

print(max(dp))