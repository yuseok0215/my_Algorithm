"""
x-1 or x+1 1초
2*x 0초


"""
import sys
from collections import deque
input = sys.stdin.readline
 
a,b = map(int,input().split())
limit = 100001
time = [0]*limit
 
def bfs(x,y):
    q = deque()
    if x == 0 :
        q.append(1)
    else :
        q.append(x)
    
    while q:
        x = q.popleft()
        if y == x :
            return time[x]
        
        for nx in (x-1,x+1,x*2):
            if 0 <= nx < limit and time[nx]==0:
                if nx == 2*x :
                    time[nx] = time[x]
                    q.appendleft(nx)
                else : 
                    time[nx] = time[x] + 1
                    q.append(nx)
 
if a==0 :
    print(bfs(a,b)+1)
else :
    print(bfs(a,b))


# 다익스트라 풀이법
# import heapq
# INF = int(1e9)

# N, K = map(int, input().split())  # 시작 위치, 도착 위치
# distance = [INF]*100001  # 100001개의 떨어진 거리

# def dijkstra(start):  # 다익스트라
#     distance[start] = 0  # 시작 위치 초기화
#     q = []
#     heapq.heappush(q, (0, start))  # 시작 위치 우선 순위 큐 삽입

#     while q:  # q에 값이 있을 동안
#         dist, now = heapq.heappop(q)  # 거리가 가장 짧은 노드
#         if distance[now] < dist:
#             continue
#         for a, b in [(now*2, dist), (now+1, dist+1), (now-1, dist+1)]:  # 2배, 오른쪽, 왼쪽
#             if 0 <= a <= 100000 and distance[a] > b:  # 범위 안에 있고 방문하지 않았다면(범위 주의)
#                 distance[a] = b
#                 heapq.heappush(q, (b, a))

# dijkstra(N)  # 시작 위치 다익스트라 실행
# print(distance[K])  # 시작 위치로부터 K가 떨어진 최소 거리

# import heapq

# n, k = map(int, input().split())

# distance = [0 for _ in range(100001)]
# visited = [[False] for _ in range(100001)]

# time = 0

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (start, 0))

#     while q:
#         x, dist = heapq.heappop(q)

#         if distance[x] < dist:
#             continue
        
            
#         for nx in (x-1, x+1, 2*x):
#             if visited[nx]:
#                 continue
            
#             if nx == 2*x:
#                 distance[nx] = distance[x]
#             else:
#                 distance[nx] = distance[x] + 1

#             visited[nx] = True
#             heapq.heappush(q, (nx, distance[nx]))

# dijkstra(n)

# print(distance[k])





 