from collections import deque

n,m,k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    q.append((a,b))

    visited[a][b] = True
    size = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    size += 1
                    q.append((nx,ny))
    
    return size

visited = [[False] * m for _ in range(n)]
answer = -1e9

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            temp = bfs(i,j)
            if temp > answer:
                answer = temp

print(answer)

    