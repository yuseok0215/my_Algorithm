import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []

for _ in range(n):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x : (x[0],x[1]))

heap = [time[0][1]]
for i in range(1,n):
    if heap[0] <= time[i][0]: 
        # 다음 시작 시간이 끝나는 시간보다 이후면
        heapq.heappop(heap)
    heapq.heappush(heap,time[i][1])

print(len(heap))

"""
1. 접근방법
일단 이 문제는 시간초과가 날 수 있기 때문에 효율을 극대화해야 했다.(사실 모든 문제를 최대 효율로 풀어야하긴 함..)
먼저 시간순으로 정렬하는 것까지는 생각할 수 있었다. 끝나는 시간을 어떻게 담고 뺴내야하는 것에서 발목을 잡혔다.

heapq을 사용하자.
1. pop했을 때 가장 작은 원소를 제거하고 반환함.
"""