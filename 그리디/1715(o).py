"""
1. 접근방법
작은 것들을 먼저 더해야 작은 값들을 여러번 더해 작은 결과값을 만들 수 있기 때문에
오름차순정렬을 하자..!
그리고 최종 횟수는 누적값이다. 근데 이게 골드? 

10 20 30 40

10+20=30
30+30=60
60+40=100 
총 190

10+20=30
30+40=70
30+70=100


10+20=30
30+40=70

10 20 40

10+20=30
30+40=70


"""
import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = []

for _ in range(n):
    card.append(int(input()))

heapq.heapify(card)

ans = 0
while len(card) > 1:
    a = heapq.heappop(card) # 10
    b = heapq.heappop(card) # 20

    tmp = a + b 

    ans = ans + tmp
    heapq.heappush(card, tmp)
    
print(ans)






