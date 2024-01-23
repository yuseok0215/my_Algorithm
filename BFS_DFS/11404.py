from collections import deque

n = int(input())
m = int(input())

bus = [[] for _ in range(m+1)]

for _ in range(m):
    a,b,c = map(int, input().split())

    bus[a].append((b,c))

def bfs(start, end):
    if start == end:
        return 0

    distance = [0 * n for _ in range(n+1)]

    q = deque()
    q.append(start)

    while q:
        x = q.popleft()

        if x == end:
            return distance[end]
        
        for nx, dist in bus[x]:
            tmp = distance[x] + dist
            if tmp < distance[nx]:
                distance[nx] = tmp
                q.append(nx)
            



answer = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        res = bfs(i,j)
        answer[i][j] = res

for elem in answer:
    print(elem, end=' ')
        
