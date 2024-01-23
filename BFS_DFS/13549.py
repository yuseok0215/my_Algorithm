"""
x-1 or x+1 1초
2**x 0초


"""
import heapq

n, k = map(int, input().split())

distance = [0 for _ in range(100001)]
visited = [[False] for _ in range(100001)]

time = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        x, dist = heapq.heappop(q)

        if distance[x] < dist:
            continue
        
            
        for nx in (x-1, x+1, 2**x):
            if visited[nx] == True:
                continue
            
            if nx == 2**x:
                distance[nx] = distance[x]
            else:
                distance[nx] = distance[x] + 1

            visited[nx] = True
            heapq.heappush(q, (nx, distance[nx]))

dijkstra(n)

print(distance[k])





 