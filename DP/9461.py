t = int(input())
for _ in range(t):
    n = int(input())

    dp = [0] * (101)
    
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[n])
"""
0
1
1
1
2
2
3
4
5
7


"""