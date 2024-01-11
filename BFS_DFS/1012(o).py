from collections import deque
    
def bfs(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split()) # m x n
    
    graph = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1

    visited = [[False] * m for _ in range(n)]
    
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    ans = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                ans += 1

    print(ans)



    
    
