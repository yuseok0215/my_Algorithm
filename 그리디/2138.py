"""
i-1, i, i+1

1,2     n-1,n

1111
 000
1000
0110 

"""

n = int(input())

current = list(map(int, input()))
target = list(map(int, input()))


def switching(a,b):
    a_copy = a[:]
    press = 0

    for i in range(1, n):

        if a_copy[i-1] == b[i-1]:
            continue
        
        press += 1
        for j in range(i-1,i+2):
            if j<n:
                a_copy[j] = 1 - a_copy[j]

    if a_copy == b:
        return press
    else:
        return 1e9
    
# 0번째 스위치를 누르지 않았을 때
result = switching(current, target)

# 0번째 스위치를 눌렀을 때
current[0] = 1 - current[0]
current[1] = 1 - current[1]

res = min(result, switching(current, target) + 1)

if res == 1e9:
    print(-1)
else:
    print(res)
        




# 001110
# 110100