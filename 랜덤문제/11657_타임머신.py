import heapq
INF = 1e9

n,m = map(int, input().split())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    bus[a].append((b,c))

# 1 -> 2 -> 3 -> 1

for i in range(2,n+1):
    # if distance[i] != 0:
    
    for end,dist in bus[i]:
        if end == 1 and dist < 0:
            print(-1)
            exit()

distance = [INF] * (n+1)

def dijkstra():
    q = []
    heapq.heappush(q, (1,0))

    while q:
        x,dist = heapq.heappop(q)

        if distance[x] < dist:
            continue

        for nx, n_dist in bus[x]:
            if distance[nx] > dist + n_dist:
                distance[nx] = dist + n_dist
                heapq.heappush(q,(nx,distance[nx]))

dijkstra()


for i in range(2,n+1):
    if distance[i] == INF:
        print(-1)
        continue
    print(distance[i])

# 1을 제외한 도시에서 출발해서 1로 다시 도착하는 노선이 있다면 -1
# 아니라면 다익스트라로 구하기....?