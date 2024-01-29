n = int(input())

physical = []
for _ in range(n):
    w,h = map(int, input().split())
    physical.append((w,h))

answer = []
for weight, height in physical:
    cnt = 0
    for w,h in physical:
        if weight < w and height < h:
            cnt += 1
    answer.append(cnt+1)

print(*answer) 


