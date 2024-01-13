"""
수빈이의 현재 점 N
동생의 현재 점 K

x+-1 혹은 2*x


5 -> 17

5 * 2 = 10
10 - 1 = 9
9 * 2 = 18
18 - 1 =17
"""
from collections import deque

MAX = 10**5

n,k = map(int, input().split())

graph = [0 for _ in range(MAX)]
max_idx = max(n,k)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()

        if x == k:
            return print(graph[x])
            break
        
        for nx in (x-1, x+1, 2*x):
            if graph[nx] == 0 and 0<=nx<=MAX:
                graph[nx] = graph[x] + 1
                q.append(nx)

bfs(n)
