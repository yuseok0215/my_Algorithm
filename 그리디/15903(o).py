"""
가장 작은 두 숫자를 고르고 바꾼뒤에 그 숫자를 덮어씌우자..!
heapq?
"""
import heapq

n,m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)

for i in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)

    sum = x+y
    heapq.heappush(cards, sum)
    heapq.heappush(cards, sum)

ans = 0
for num in cards:
    ans += num

print(ans)