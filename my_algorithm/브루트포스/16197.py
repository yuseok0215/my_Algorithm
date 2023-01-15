import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
coins = []
for i in range(n):
    temp = list(input().strip())
    graph.append(temp)
    for j in range(m):
        if temp[i][j] == 'o':
            coins.append((i,j))
        
dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer = 0


def dfs(x1,y1,x2,y2,cnt):
    if cnt > 10:
        return print(-1)

    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]

        if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:
            if graph[nx1][ny1] == "#":
                nx1, ny1 = x1, y1
            if graph[nx2][ny2] == "#":
                nx2, ny2 = x2, y2
            dfs(nx1, ny1, nx2, ny2, cnt+1)
        elif 0<=nx1<n and 0<=ny1<m:
            return cnt+1
        elif 0<=nx2<n and 0<=ny2<m:
            return cnt+1
        else: # 둘다 빠진 경우
            return -1

ans = dfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)

print(ans)

