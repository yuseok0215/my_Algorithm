"""
dfs로만 풀 수 있는 문제..

"""
import sys

sys.setrecursionlimit(10**9)

r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            alphas.remove(maps[nx][ny])
alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)

"""
global [변수명] 으로 재귀 함수 내에서 값 비교 가능

"""





# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# visited = [[False] * c for _ in range(r)]
# visited_alp = []

# def bfs(a,b):
#     q = deque()
#     q.append((a,b))

#     cnt = 1
#     while q:
#         x,y = q.popleft()

#         visited_alp.append(graph[x][y])

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0<=nx<r and 0<=ny<c:
#                 if not visited[nx][ny] and graph[nx][ny] not in visited_alp:
#                     visited[nx][ny] = True
#                     cnt += 1
#                     q.append((nx,ny))
#     return cnt

# print(bfs(0,0))
        
