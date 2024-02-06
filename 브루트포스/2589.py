import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

max_time = -1e9

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b,t):
    q = deque()
    q.append((a,b,t))
    visited[a][b] = True

    while q:
        x,y,time = q.popleft()

        t = max(t, time)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 'L':
                    visited[nx][ny] = True
                    q.append((nx,ny,time+1))
    
    return t

                    


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[False] * m for _ in range(n)]
            max_time = max(max_time, bfs(i,j,0))

print(max_time)