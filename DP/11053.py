n = int(input())
nums = list(map(int, input().split()))

dp = [0] * 1001

for i in range(n):
    for j in range(n):
        