import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

parent = [0] * (n+1)

while queue:
    n = queue.popleft()
    for nx in graph[n]:
        if parent[nx] == 0:
            parent[nx] = n
            queue.append(nx)

ans = parent[2:]
for elem in ans:
    print(elem)

"""
[1] 6 4

[2] 4
[3] 6 5
[4] 1 2 7
[5] 3
[6] 1 3
[7] 4

"""