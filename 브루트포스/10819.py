from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

arr = permutations(nums)

ans = 0

for elem in arr:
    s = 0
    for i in range(len(elem)-1):
        s += abs(elem[i]-elem[i+1])
    if s > ans:
        ans = s

print(ans)
