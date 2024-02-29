import sys
input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))

answer = []

plus = []
minus = []

for elem in liq:
    if elem > 0:
        plus.append(elem)
    else:
        minus.append(elem)

plus.sort() # 4, 98
minus.sort(reverse=True) # -1,-2,-99

if len(plus) == n:
    print(answer.pop(0), end=' ')
    print(answer.pop(0))
    exit(0)
elif len(minus) == n:
    print(answer.pop(0), end=' ')
    print(answer.pop(0))
    exit(0)

_min = 1e9
for a in plus:
    for b in minus:
        if 2*a < abs(b):
            break
        if abs(a+b) < _min:
            _min = abs(a+b)
            answer.append((b,a))

print(answer[-1][0], end=' ')
print(answer[-1][1])
