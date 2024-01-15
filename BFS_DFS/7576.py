"""
하루가 지나면, 익은 토마토의 인접한 토마토도 익는다..
며칠이 지나면 다 익게 되는지 

"""
from collections import deque

m,n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

if not any(0 in row for row in graph):
    print(0)    

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # if nx<0 or nx>=n or ny<0 or ny<=m:
            #     continue

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))

bfs()

day = 0
for row in graph:
    for i in row:
        if i == 0:  # 익지 않은 토마토가 있으면(=토마토가 모두 익지 못하는 상황) -1 출력
            print(-1)
            exit() # 다음 행의 여부와 관계 없이 -1만 출력해야하므로 종료시킴
    else: # 그래프에서 가장 큰 값이 마지막으로 익은 토마토임 → 한 줄씩 최댓값을 day로 갱신하며 최댓값 찾기
        day = max(day, max(row)) 

print(day-1)








# while True:
#     visited = [[False]*m for _ in range(n)]

#     flag = False
#     for i in range(n):
#         for j in range(m):
#             if not visited[i][j] and graph[i][j] == 1:
#                 tmp = bfs(i,j) 
#                 if tmp > 0:
#                     flag = True

#     if any(0 in row for row in graph) and not flag:
#         print(-1)
#         break

#     days += 1

#     if not any(0 in row for row in graph): # any(): 하나 이상의 요소가 참이면 True
#         print(days)
#         break




    
