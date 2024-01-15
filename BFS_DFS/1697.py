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
import sys
from collections import deque

input = sys.stdin.readline


n,k = map(int, input().split())

graph = [0 for _ in range(100001)]

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()

        if x == k:
            return print(graph[x])
        
        for nx in (x-1, x+1, 2*x):
            if 0<=nx<=100000 and graph[nx] == 0: # AND는 순차적으로 돌기 떄문에 우선순위가 높은 것을 앞으로 둬야 시간이 빨라진다..
                graph[nx] = graph[x] + 1
                q.append(nx)

bfs(n)
