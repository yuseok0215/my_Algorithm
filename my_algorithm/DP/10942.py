import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

#dp
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for start in range(n-i):
        end = start + i

        if start == end:
            dp[start][end] = 1
        elif nums[start] == nums[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for i in range(m):
    s,e = map(int, input().split())
    print(dp[s-1][e-1])