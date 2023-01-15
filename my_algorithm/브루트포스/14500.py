n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

result = []

dx = [0,0,1,-1]
dy = [-1,1,0,0]

maxValue = 0

def dfs(x, y, cnt, sum):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, sum)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, sum+graph[nx][ny])
            visited[nx][ny] = False

def other(x,y):
    global maxValue
    for i in range(4):
        tmp = graph[x][y]
        for j in range(3):
            t = (i+j)%4 # 012, 013, 123, 023
            nx = x + dx[t]
            ny = y + dy[t]

            if 0<=nx<n and 0<=ny<m:
                tmp += graph[nx][ny]
            else:
                break
        
        maxValue = max(maxValue, tmp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
        other(i,j)

print(maxValue)