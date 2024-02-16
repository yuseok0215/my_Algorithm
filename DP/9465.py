"""
n번째에서 내가 둘중에 어떤 것을 선택하느냐.
그리고 선택한 것을 두고 n-1, n-2는 어떻게 배치할 수 있는가

"""

t = int(input())
for _ in range(t):
    n = int(input())

    stick = []
    for i in range(2):
        stick.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(2)]

     # 스티커 길이가 1일 경우
    dp[0][0] = stick[0][0]
    dp[1][0] = stick[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # 스티커 길이가 2일 경우
    dp[0][1] = stick[1][0] + stick[0][1]
    dp[1][1] = stick[0][0] + stick[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    # 스티커 길이가 3이상일 경우
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + stick[0][i]
        # 내가 i번째 1행을 선택했다면 -> i-1 2행과 i-2 2행중 어떤것이 더 크냐. 
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + stick[1][i]

    print(max(dp[0][-1], dp[1][-1]))

# https://jyeonnyang2.tistory.com/42 예시로 질문하기


