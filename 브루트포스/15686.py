import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
chicken = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            chicken.append((i,j))
    graph.append(temp)

chicken_dist = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    q.append((a,b,0))

    visited = [[False] * n for _ in range(n)]
    
    while q:
        x,y,dist = q.popleft()
        visited[x][y] = True

        if graph[x][y] == 2:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,dist+1)) 


def check_dist(graph):
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result += bfs(i,j)
    
    return result
                

def pick_chicken(cnt):
    global answer

    if cnt == len(chicken)-m:
        answer.append(check_dist(graph))

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                graph[i][j] = 0
                pick_chicken(cnt + 1)
                graph[i][j] = 2
    
answer = []

pick_chicken(0)

print(min(answer))
                
                



