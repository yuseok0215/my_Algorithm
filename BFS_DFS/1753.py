"""
방향 그래프이다.
다익스트라 알고리즘을 이용해야했던 문제이다.
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        #현재 노드와 연결된 인접 노드 확인
        for next, nv in graph[now]:
            cost =dist+ nv
            if cost < distance[next] :
                distance[next] = cost
                heapq.heappush(q,(cost,next))


#V == 5일 때 1~5까지 노드가 있는거임.
V, E = map(int,input().split())

snode = int(input()) #시작 노드

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1) #최단 거리 테이블
#연결 정보 입력
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


dijkstra(snode)

#i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

# from collections import deque

# n,e = map(int, input().split())
# k = int(input()) # 시작정점의 번호

# graph = [[] for _ in range(n+1)]
# for _ in range(e):
#     u,v,w = map(int, input().split())

#     graph[u].append((v,w))


# def bfs(end):
#     global result

#     if end == k:
#         result = 0
#         return True
    
#     q = deque()
#     q.append((k,0))

#     while q:
#         x, res = q.popleft()

#         if x == end:
#             result = min(res, result)

#         for nx, nv in graph[x]:
#             res += nv
#             q.append((nx,res))
#             res -= nv
    
#     if result == 1e9:
#         return False
#     else:
#         return True
   
# for i in range(1, n+1):
#     result = 1e9
#     if bfs(i):
#         print(result)
#     else:
#         print('INF')



