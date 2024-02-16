import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = []

dp = [0] * 10001

for _ in range(n):
    coins.append(int(input()))

coins.sort()

# for i in range(1,n+1):
#     for coin in coins:
#         if i <= coin:
#             dp[i] += 1

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]


"""
    1 2 3 4 5 6 7 8 9 10
1   o o o o o o o o o   o 
2     o   o   o   o    o
5           o          o
 
"""
