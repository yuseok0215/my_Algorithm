n = int(input())

dp = [0] * 91

dp[1] = 1


for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

# 참고 풀이 https://cijbest.tistory.com/17