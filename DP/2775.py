t = int(input())

for _ in range(t):
    k = int(input()) # k층
    n = int(input()) # n호

    dp = [[0] * (n+1) for _ in range(k+1)]
    
    for i in range(1, n+1): # 0층 세팅
        dp[0][i] = i
    
    for i in range(1, k+1):
        for j in range(1, n+1):
            cnt = 0
            for l in range(1,j+1):
                cnt += dp[i-1][l]
            dp[i][j] = cnt
    
    print(dp[k][n])
                