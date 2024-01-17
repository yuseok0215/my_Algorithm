from collections import deque

t = int(input())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

for _ in range(t):
    l = int(input())
    graph = [[0]*l for _ in range(l)]

    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    if now_x == target_x and now_y == target_y:
        print(0)
        continue

    q = deque()
    q.append((now_x, now_y))

    while q:
        x,y = q.popleft()
        
        flag = False
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
                    if nx==target_x and ny==target_y:
                        flag=True

        if flag:
            break

    print(graph[target_x][target_y])
