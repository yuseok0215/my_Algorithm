n = int(input())
budget = list(map(int, input().split()))
k = int(input())

start, end = 1, max(budget) #이분탐색 검색 범위 설정

while start <= end: 
    mid = (start+end) // 2
    
    total = 0
    for num in budget:
        if num >= mid:
            total += mid
        else:
            total += num
    
    if total <= k:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)