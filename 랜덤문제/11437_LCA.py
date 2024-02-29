from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1] * (n+1)

def bfs():
    q = deque()
    q.append((1,1))
    parent[1] = 0

    while q:
        x = q.popleft()
        
        for nx in graph[x]:
            if parent[nx] == -1:
                parent[nx] = x
                q.append(nx)

def find_parent(k):
    q = deque()
    q.append(k)

    result = [k]

    while q:
        x = q.popleft()

        if parent[x] != 0:
            q.append(parent[x])
            result.append(parent[x])
    
    return result


bfs() # 부모노드에 대한 정보 업데이트



m = int(input())
for _ in range(m):
    a,b = map(int, input().split())

    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if len(parent_a) <= len(parent_b):
        for i in parent_a:
            if i in parent_b:
                print(i)
                break 
    elif len(parent_b) < len(parent_a):
        for i in parent_b:
            if i in parent_a:
                print(i)
                break 
    
# 93퍼센트 시간초과

# 정답
import sys
sys.setrecursionlimit(100000)

n = int(input())
parent = [0] * (n + 1)      # 각 노드의 부모 노드 정보
d = [0] * (n + 1)           # 각 노드까지의 깊이
visited = [0] * (n + 1)     # 방문 여부
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 루트 노드부터의 깊이 구하기
def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for node in graph[x]:
        if visited[node]:
            continue
        parent[node] = x
        dfs(node, depth + 1)


# 최소 공통 조상 찾기
def lca(a, b):
    # 깊이 맞추기
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드 맞추기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))