"""
1. 인접한 0의 개수만큼 -한다.
2. 빙산이 두개로 나눠졌는지 확인한다.

"""
import copy
from collections import deque

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs1(graph):
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                q.append((i,j))
    p = copy.deepcopy(q)

    while q:
        cnt = 0
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and (nx,ny) not in p:
                    cnt += 1
        
        if graph[x][y] - cnt >= 0:
            graph[x][y] -= cnt
        else:
            graph[x][y] = 0
        
def bfs2(a,b, visited):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))


def check(graph):
    visited = [[False] * m for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j ]:
                bfs2(i,j,visited)
                cnt += 1
                if cnt >= 2:
                    return cnt
    
    return cnt

year = 0
while True:
    bfs1(graph)
    year += 1

    tmp = check(graph)

    if tmp > 1:
        print(year)
        break
    elif tmp == 0:
        print(0)
        break

