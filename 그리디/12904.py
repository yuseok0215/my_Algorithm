"""
처음 주어진 두가지 방법을 이용해서 찾기에는 경우의 수가 많아보여 
조건을 뒤집어서 t -> s로 찾아가는 방법을 이용했다.

1. 문자열 뒤에 A를 삭제한다.
2. B를 삭제하고 문자열을 뒤집는다.
"""

import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

for _ in range (len(t)-len(s)):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]

if t == s:
    print(1)
else:
    print(0)
