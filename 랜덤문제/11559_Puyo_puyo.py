from collections import deque

HEIGHT = 12
WIDTH = 6

graph = []
for _ in range(12):
    graph.append(list(input()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    remove_idx = []
    q.append((a,b))
    remove_idx.append((a,b))
    

    alp = graph[a][b]
    visited[a][b] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<HEIGHT and 0<=ny<WIDTH:
                if not visited[nx][ny] and graph[nx][ny] == alp:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    remove_idx.append((nx,ny))    
                    
    if len(remove_idx) >= 4:
        for rx, ry in remove_idx:
            graph[rx][ry] = '.'
        return False
    else:
        return True
    
def drop():
    # for j in range(WIDTH):
    #     for i in range(HEIGHT-1, -1, -1):
    #         if graph[i][j] == '.':
    #             for k in range(i, HEIGHT):
    #                 if graph[k][j] != '.': # 교환
    #                     graph[i][j] = graph[k][j] 
    #                     graph[k][j] = '.'    
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if graph[j][i] != "." and graph[k][i] == ".":
                    graph[k][i] = graph[j][i]
                    graph[j][i] = "."
                    break

t = 0
while True:

    visited = [[False] * WIDTH for _ in range(HEIGHT)]

    cnt = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if not visited[i][j] and graph[i][j] != '.':
                if not bfs(i,j): # 부실 것이 있었다.
                    cnt += 1     

    drop()
    
    if cnt == 0: # 부실 수 있는 것이 없다.
        break

    t += 1

print(t)
