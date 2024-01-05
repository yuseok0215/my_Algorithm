import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

if k >= n: # 집중국이 센서개수만큼 있을 때 거리는 필요없다.(안했을 시에 런타임에러...)
    print(0)
    sys.exit()

sensor = list(map(int, input().split()))
sensor.sort()

dist = []
for i in range(n-1):
    dist.append(sensor[i+1]-sensor[i])

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))

"""
1 3 6 6 7 9
각각의 거리를 구한다.
2 3 0 1 2 
여기서 k-1개의 연결고리를 제거한다. ex) 2-1 = 1
당연히 제일 거리가 긴 것부터 없앤다.
(2) (0 1 2) 이렇게 두묶음이 생겨서 집중국을 배치할 수 있다.

이문제에서 구해야 하는 것은 집중국 수신거리의 최소값이었다.
거리의 최솟값? 그럼 일단 센서들의 거리부터 다 구한 뒤에 어떻게 집중국을 배치할까?
집중국이 3개면 연결되는 부분을 2번 짜르면 3묶음이 나오네?
그럼 최대한 거리가 긴 애들을 자르면 최솟값이 나오겠다!

이러한 접근방법을 생각해냈어야 했다.

일단 많은 문제를 다루면서 상황에 대한 데이터를 쌓는 것이 필요하다는 것을 느꼈다..
"""