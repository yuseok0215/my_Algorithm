import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (1001)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])

"""
n-1번째가 비어있다면 세로로 하나밖에 못 놓는다.
n-2번째가 비어있다면 세로 세로 혹은 가로 가로 인데
세로세로는 n-1에서 세어줬기 때문에 dp[i-2] 만 더해준다.

"""