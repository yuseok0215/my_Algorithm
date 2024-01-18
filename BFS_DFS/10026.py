from collections import deque

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b,color):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx,ny))

visited = [[False] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j, graph[i][j])
            cnt += 1
print(cnt, end = ' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j, graph[i][j])
            cnt += 1
print(cnt)
