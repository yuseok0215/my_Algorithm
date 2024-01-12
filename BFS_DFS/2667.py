from collections import deque

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    count = 1

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0>nx or n<=nx or 0>ny or n<=ny:
                continue
                
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                count += 1
                q.append((nx,ny))
    
    return count

ans = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            ans.append(bfs(i,j))

ans.sort()

print(len(ans))
for elem in ans:
    print(elem)