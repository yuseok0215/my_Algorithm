import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p,c,v = map(int, input().split())

    tree[p].append([c,v]) 
    tree[c].append([p,v])

def dfs(x, dist):
    for nx, v in tree[x]:
        if distance[nx] == -1:
            distance[nx] = dist + v
            dfs(nx, dist + v)

distance = [-1] * (n+1) # 지나온 거리를 담아줄 배열
distance[1] = 0
dfs(1,0)

start = distance.index(max(distance)) # 1번 노드에서 가장 먼 노드
distance = [-1] * (n+1)
distance[start] = 0
dfs(start,0)

print(max(distance))




# ans = 0
# case = []
# def dfs(x,ans):
#     #global ans

#     if not tree[x]:
#         case.append([ans, x])
#         return

#     for nx, v in tree[x]:
#         tree[nx][1] = tree[x][1] + v
#         dfs(nx[0],ans)
#         # ans -= nx[1] # 깊이 탐색했다가 다시 다른 깊이를 탐색할때 이전에 더해준 가중치는 없어져야 한다.(백트래킹)

# dfs(1,0)
# sorted_case = sorted(case, key=lambda x: x[0])





# BFS로는 답을 찾을 수 없는 문제..
# ans = 0
# case = []
# def bfs(start):
#     global ans
#     q = deque()
#     q.append(start)

#     while q:
#         x = q.popleft()

#         if not tree[x]:
#             case.append(ans)

#         for nx in tree[x]:
#             ans += nx[1]
#             q.append(nx[0])

# bfs(1)

# print(case)
