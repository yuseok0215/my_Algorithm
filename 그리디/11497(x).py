
t = int(input())
for _ in range(t):
    n = int(input())

    height = list(map(int, input().split()))
    height.sort()
    ans = 0
    for i in range(2, n):
        res = max(res, abs(height[i] - height[i-2]))
    print(ans)

"""
1. 접근방법 

      1(1)
  5(3)    3(2)
2(5)        4(4)

        13
    12      12
11              11



2 4 5 7 9
 2 1 2 2
"""
