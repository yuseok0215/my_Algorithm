n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

_dict = {}
for i in range(n):
    if a[i] in _dict:
        _dict[a[i]] += 1 
    else:
        _dict[a[i]] = 1

for j in range(m):
    if b[j] not in _dict:
        print(0, end = ' ')
    else:
        print(_dict[b[j]], end=' ')

# 정렬 후에 이분탐색 메서드를 정의해서 각 숫자를 비교해본다.