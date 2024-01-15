"""
0 2 4 4 -> (2,0~3) (1,0~3) 2-0 4-0
1 1 2 5 -> (0~3,1)
4 0 6 2 -> (3,4~5) (4,4~5)

"""

from collections import deque

m,n,k = map(int, input().split())

graph = [[0]*n for _ in range(m)]

arr = [] 
for _ in range(k): # 중요했던 부분
    x1, y1, x2, y2 = map(int, input().split()) # 0 2 4 4
    for i in range(m-y2, m-y1):
        for j in range(x1, x2):
            graph[i][j] = 1
    
# for l in arr:
#     x1,y1,x2,y2 = l
#     start_x = m-y2 # 5-4 = 1
#     end_x = m-y1-1 # 5-2-1 = 2
#     start_y = x1 # 0
#     end_y = x2-1 # 4-1 = 3 

#     for i in range(start_x, end_x+1):
#         for j in range(start_y, end_y+1):
#             graph[i][j] = 1


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    
    cnt = 1
    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<m and 0<=ny<n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    return cnt

visited = [[False] * n for _ in range(m)]

answer =  []
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 0:
            answer.append(bfs(i,j))

print(len(answer))
answer.sort()
for elem in answer:
    print(elem, end=' ')
            