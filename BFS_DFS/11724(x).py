from collections import deque 

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)

"""
6 (5 1 2) 3 4 6 

"""