from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    q.append((a,b))

    cnt = 1
    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx,ny))
    return cnt

visited = [[False]*m for _ in range(n)]

ans = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            tmp = bfs(i,j)
            cnt += 1
            if ans < tmp:
                ans = tmp

print(cnt)
print(ans)