"""
1. 접근방법

"""
n,k = map(int, input().split())

x = 1
ans = 0
while True:
    standard = k * (2**x)

    if n <= standard:
       ans = standard - n
       break

    x+=1

print(ans)