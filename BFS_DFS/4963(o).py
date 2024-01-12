from collections import deque

dx = [0,0,-1,1,1,1,-1,-1]
dy = [-1,1,0,0,1,-1,1,-1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    
    while q:
        x,y = q.popleft()
        visited[x][y] = True    
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))



while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    
    print(cnt)

