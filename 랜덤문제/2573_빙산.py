from collections import deque

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def melting():
    global graph
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                q.append((i,j))

    melting_point = []
    while q:
        x,y = q.popleft()

        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    cnt += 1

        melting_point.append((x,y,cnt))


    for x,y,cnt in melting_point:
        graph[x][y] = max(0, graph[x][y] - cnt)


def check():

    visited = [[False] * m for _ in range(n)]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                visited = bfs(i,j,visited)
                cnt += 1
    
    return cnt

def bfs(a,b,visited):
    q = deque()
    q.append((a,b))

    visited[a][b] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))    
                    
    return visited
    
time = 0

while True:

    melting()
    time += 1

    flag = check()

    if flag >= 2:
        print(time)
        break
    elif flag == 0:
        print(0)
        break