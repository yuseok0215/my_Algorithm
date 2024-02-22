import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

_dict = {}
for i in range(n):
    _dict[a[i]] = a.count(a[i])

for j in range(m):
    if b[j] not in _dict:
        print(0, end = ' ')
    else:
        print(_dict[b[j]], end=' ')
