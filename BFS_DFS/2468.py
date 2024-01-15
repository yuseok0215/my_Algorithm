from collections import deque

n = int(input())

max_h = 0
graph = []
for _ in range(n):
    tmp_list = list(map(int, input().split()))
    graph.append(tmp_list)
    if max_h < max(tmp_list):
        max_h = max(tmp_list)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(height,a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if not visited[nx][ny] and graph[nx][ny] > height:
                visited[nx][ny] = True
                q.append((nx,ny))

answer = 0
for height in range(max_h+1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > height:
                bfs(height,i,j)
                cnt += 1
    if answer < cnt:
        answer = cnt

print(answer)
                
            

