"""


"""
import heapq
import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    k = int(input())

    paper = list(map(int, input().split()))

    heapq.heapify(paper)

    answer = 0
    while len(paper) > 1:
        a = heapq.heappop(paper)
        b = heapq.heappop(paper)

        answer += a+b
        heapq.heappush(paper, a+b)
    
    print(answer)