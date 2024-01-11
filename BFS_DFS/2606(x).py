"""
1. BFS의 접근법
"""
# from collections import deque

# m = int(input()) # 컴퓨터 개수
# n = int(input()) # 연결선 개수

# graph = [[] for i in range(m+1)] # 그래프 초기화
# visited = [False] * (m+1)

# for _ in range(n):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited[1] = True # 방문

# cnt = 0
# q = deque([1])

# while q:
#     x = q.popleft()
#     for nx in graph[x]:
#         if not visited[nx]:
#             q.append(nx)
#             visited[nx] = True
#             cnt += 1
# print(sum(visited)-1)

"""
1. DFS의 접근법
"""
m = int(input()) # 컴퓨터 개수
n = int(input()) # 연결선 개수

graph = [[] for i in range(m+1)] # 그래프 초기화
visited = [False] * (m+1)

for _ in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, cnt):
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            cnt = dfs(nx, cnt+1)
    return cnt

print(dfs(1,0))