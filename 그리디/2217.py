n = int(input())

rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort()


max_weight = 0
for i in range(n):
    if max_weight < rope[i] * (n-i):
        max_weight = rope[i] * (n-i)

print(max_weight)
    
"""
N개의 로프
k개의 로프를 사용하여 중량 w인 물체를 들어올려라
여러개의 로프를 매달았을 때 w/k만큼 중량이 걸린다.

이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해보자

1. 접근방법
- 가장 많은 로프를 사용하는 경우: 가장 낮은 지탱무게를 가진 로프를 기준으로 로프의 개수만큼 곱하기
하지만 로프의 중량을 높게 설정해서 적은 로프로도 높은 결과를 만들어낼 수 있을 것 같다.

그럼 가장 낮은 중량의 로프부터 높은 중량으로 가면서 최대중량을 업데이트하면 나오지 않을까?

3. 시간복잡도
O(nlogn) 정렬
"""
