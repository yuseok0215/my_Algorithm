n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))

answer = num[0]
_min = int(1e9)
_max = -int(1e9)

def dfs(index):
    global answer
    global _min, _max 

    if index == n:
        if answer > _max:
            _max = answer
        if answer < _min:
            _min = answer 
        return

    for i in range(4):
        tmp = answer
        if oper[i] > 0:
            if i==0:
                answer += num[index]
            elif i==1:
                answer -= num[index]
            elif i==2:
                answer *= num[index]
            else:
                if answer >= 0:
                    answer //= num[index]
                else:
                    answer = (-answer // num[index]) * -1

        oper[i] -= 1
        dfs(index+1)
        answer = tmp
        oper[i] += 1
    
dfs(1)
print(_max)
print(_min)
