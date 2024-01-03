n = int(input())
distance = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

purchase_index = 0 # 구매하는 주유소의 인덱스
purchase_distance = 0 # 구매하는 거리
total_price = 0


for i in range(n-1):
    if oil_price[purchase_index] > oil_price[i]: # 현재 주유소보다 더 저렴한 주유소를 도달했을 때
        total_price += oil_price[purchase_index]*purchase_distance 
        purchase_index = i # 구매하는 주유소를 다시 현재 위치로 업데이트
        purchase_distance = 0 # 구매하는 거리를 초기화

    purchase_distance += distance[i]    
        
    if i == n-2: 
        # 만약에 마지막 주유소 이동거리까지 합산했을 떄
        total_price += oil_price[purchase_index]*purchase_distance
        # 구매하는 주유소에서 마지막 남은 거리를 구매한다.

print(total_price)

"""
n개의 도시, 일직선 도로 위에 있음

1. 접근방법

일단 가장 가격이 싼 주유소를 찾는게 먼저겠지!?
그리고 그 싼 주유소에 최소 비용으로 도착한 뒤에 남은 이동거리에 따라 기름을 구입하면 될 것 같다!(잘못됨)
-> 그 싼 주유소가 뒤쪽에 배치되면 더 비용이 많이 든다.

각 위치에서 뒤쪽 주유소의 가격을 확인했을 때 나보다 더 저렴한 주유소까지 가는 거리만큼만 구매하면 된다.

3. 시간복잡도
O(n)

"""