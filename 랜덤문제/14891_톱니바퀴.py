wheels = []

for _ in range(4):
    wheels.append(list(input()))

k = int(input())

def rotate_right(num):
    last = wheels[num][7]
    for i in range(7,0,-1):
        wheels[num][i] = wheels[num][i-1]
    wheels[num][0] = last

def rotate_left(num):
    first = wheels[num][0]
    for i in range(7):
        wheels[num][i] = wheels[num][i+1]
    wheels[num][7] = first


for _ in range(k):
    a,b = map(int, input().split())
    
    if b==1: # 시계 방향
        rotate_right(a-1)
        if a-2 >= 0:
            rotate_left(a-2)
        if a <= 3:
            rotate_left(a)


    elif b==-1: # 반시계 방향
        rotate_left(a-1)
        if a-2 >= 0:
            rotate_right(a-2)
        if a <= 3:
            rotate_right(a)

res = 0
for i in range(4):
    if wheels[i][0] == 1:
        res += 2**i
print(res)
        