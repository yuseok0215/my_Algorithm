import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
chicken = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            chicken.append((i,j))
    graph.append(temp)

chicken_dist = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b):
    q = deque()
    q.append((a,b,0))

    visited = [[False] * n for _ in range(n)]
    
    while q:
        x,y,dist = q.popleft()
        visited[x][y] = True

        if graph[x][y] == 2:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,dist+1)) 

def check_dist(graph):
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result += bfs(i,j)
    
    return result

def pick_chicken(cnt):
    global answer

    if cnt == len(chicken)-m:
        answer.append(check_dist(graph))

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                graph[i][j] = 0
                pick_chicken(cnt + 1)
                graph[i][j] = 2
    
answer = []

pick_chicken(0)

print(min(answer))

# 빠른 풀이 ..
    # import sys
    # from itertools import combinations

    # input = sys.stdin.readline

    # n, m = map(int, input().split())
    # city = list(list(map(int, input().split())) for _ in range(n))
    # result = 999999
    # house = []      # 집의 좌표
    # chick = []      # 치킨집의 좌표

    # for i in range(n):
    #     for j in range(n):
    #         if city[i][j] == 1:
    #             house.append([i, j])
    #         elif city[i][j] == 2:
    #             chick.append([i, j])

    # for chi in combinations(chick, m):  # m개의 치킨집 선택
    #     temp = 0            # 도시의 치킨 거리
    #     for h in house: 
    #         chi_len = 999   # 각 집마다 치킨 거리
    #         for j in range(m):
    #             chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
    #         temp += chi_len
    #     result = min(result, temp)

    # print(result)   



