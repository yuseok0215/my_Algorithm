"""
n=1 0~9 10
n=2 0(0~9) 1(1~9) 2(2~9)55
n=3 00(0~9) 01(1~9) 10 +  + 1
    11(1~9) 12(2~9) 9 +  + 1
    22(2~0)       8+ +1
"""

import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10

for i in range(n-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)