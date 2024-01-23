from collections import deque

n,m = map(int, input().split())

graph = []
virus_index = []
for i in range(n):
    tmp_list = list(map(int, input().split()))
    for j in range(m):
        if tmp_list[j] == 2:
            virus_index.append((i,j))

dx = [0,0,-1,1]
dy = [-1,1,0,0]    

def spread_virus(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx,ny))

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            graph[i][j] = 1
            cnt += 1
    