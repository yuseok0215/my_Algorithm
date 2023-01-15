n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))

def sol(i, k, result):
    while i > 0:
        result -= num[k]
        i -= 1
        k += 1
    return k

result = num[0]
k = sol(oper[1], 1, result)
sol(oper[3], k, result)
sol(oper[0], k, result)
sol(oper[2], k, result)
print(result)