k,n = map(int, input().split())
len_ = []

for _ in range(k):
    len_.append(int(input()))

start,end = 1, max(len_)

while start <= end: 
    mid = (start+end) // 2

    cnt = 0
    for length in len_:
        cnt += length // mid
    
    if cnt < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)