import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

oper_cnt = sum(oper)

temp = []
_max = 0
_min = 1e9
def run_oper(temp, i, result):
    if temp[i-1] == 0:
        result += nums[i]
    elif temp[i-1] == 1:
        result -= nums[i]
    elif temp[i-1] == 2:
        result *= nums[i]
    elif temp[i-1] == 3:
        if result >= 0:
            result //= nums[i]
        else:
            result = -result // nums[i]
            result = -result
    
    return result

def dfs():
    global _max
    global _min

    if len(temp) == oper_cnt:
        result = nums[0]
        for i in range(1,n):
            result = run_oper(temp, i, result)
        _max = max(_max, result)
        _min = min(_min, result)    

    idx = 0
    cnt = 0
    while sum(oper) > 0:
        if cnt == oper_cnt:
            break

        idx %= 4

        if oper[idx] >= 1:
            oper[idx] -=1
            temp.append(idx)
            cnt += 1
            dfs()
            temp.pop()
            oper[idx] += 1
        
        idx += 1


dfs()

print(_max)
print(_min)



# 시간초과 안나는 깔끔한 식
# 백트래킹 (Python3 통과, PyPy3도 통과)
# import sys

# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # +, -, *, //

# maximum = -1e9
# minimum = 1e9


# def dfs(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return

#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


# dfs(1, num[0], op[0], op[1], op[2], op[3])
# print(maximum)