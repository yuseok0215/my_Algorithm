"""
n명 (짝수) / 
"""

import sys
input = sys.stdin.readline

n = int(input())

power = []
for _ in range(n):
    power.append(list(map(int, input().split())))

cnt = n // 2

start = []
link = []
answer = 1e9

visited = [False for _ in range(n)]

def dfs(k, idx): # k = 한팀의 인원수 /
    global answer
    if k == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += power[i][j]
                elif not visited[i] and not visited[j]:
                    link += power[i][j]
        
        answer = min(answer, abs(start - link))

    for i in range(idx, n): # 백트래킹을 이용한 순열 찾기
        if not visited[i]:
            visited[i] = True
            dfs(k+1, i+1)
            visited[i] = False
    
dfs(0,0)
print(answer)