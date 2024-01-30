"""


"""
from collections import deque

n = int(input()) # 노드의 개수
parent = list(map(int, input().split())) # 부모가 없다면 -1로 즉 최상위 노드
remove_node = int(input()) # 지울 노드의 번호

def dfs(rn):
    parent[rn] = -2
    for i in range(n):
        if parent[i] == rn:
            dfs(i)
            
dfs(remove_node)

cnt = 0
for i in range(len(parent)):
    if parent[i] != -2 and i not in parent:
        cnt += 1   

print(cnt)