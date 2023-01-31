n,m = map(int, input().split())
w = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if w[i] != w[j]:
            cnt += 1

print(cnt)