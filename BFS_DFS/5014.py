"""
스타트링크 총 f층
스타트링크 위치 g층
강호 s층
위로 u층을 가는 버튼
아래로 d층을 가는 버튼
"""
import sys
from collections import deque

input = sys.stdin.readline

f,s,g,u,d = map(int, input().split())
graph = [0] * (f+1)
# visited = [0] * (f+1)

def bfs(k):
    q = deque()
    q.append(k)
    # visited[k] = 1

    while q:
        x = q.popleft()

        if x == g:
            return graph[g]
            

        for nx in (x-d, x+u):
            if 0<nx<=f and graph[nx] == 0:
                # visited[nx] = 1
                graph[nx] = graph[x] + 1
                q.append(nx)
    if graph[g] == 0:
        return "use the stairs"
    

print(bfs(s))
