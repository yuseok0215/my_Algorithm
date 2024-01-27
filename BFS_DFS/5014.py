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

def bfs(k):
    q = deque()
    q.append(k)

    graph[k] = 1 # 처음 있던자리도 방문처리를 해줘야하기 때문에 1을 넣어줬어야 했다.
 
    while q:
        x = q.popleft()

        if x == g:
            return graph[g] - 1
            

        for nx in (x-d, x+u):
            if 0<nx<=f and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                q.append(nx)
                
    if graph[g] == 0:
        return "use the stairs"
    

print(bfs(s))
