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

# 라이브러리 X
n = int(input())
in_list = list(map(int ,input().split()))
visited = [False]*n
answer = 0

def sol(li):
  global answer

  if len(li) == n:
    total = 0
    for i in range(n-1):
      total += abs(li[i]- li[i+1])

    answer = max(answer, total)
    return

  for i in range(n): # 모든 순열 체킹(백트래킹으로) # 1 15 8 4 10 20
    if not visited[i]: # if in_list[i] not in li
      visited[i] = True 
      li.append(in_list[i]) # 1

      sol(li) 
      
      visited[i] = False
      li.pop()

sol([])
print(answer)