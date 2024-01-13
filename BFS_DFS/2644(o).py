"""
BFS_DFS를 사용하면서 바로 7->3으로의 촌수를 계산하는 것이 아니라
일단 BFS_DFS로 7에서 모든 관계로 이동하는 모든 촌수를 구해놓은 후에 타겟에 대한 
촌수 값을 구하는 문제였다..!

시간복잡도
n^2
"""
from collections import deque

n = int(input()) # 전체 사람 수
a,b = map(int, input().split())
m = int(input())

relation = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

visited = [0 for _ in range(n+1)]


# def dfs(node):
#     for next_node in relation[node]:
#         if visited[next_node] == 0:
#             visited[next_node] = visited[node] + 1
#             dfs(next_node)     

# dfs(a)
# print(visited[b] if visited[b] > 0 else -1)


def bfs(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()

        for next_node in relation[node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[node] + 1
                q.append(next_node)

bfs(a)
print(visited[b] if visited[b] > 0 else -1)

