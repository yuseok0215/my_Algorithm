"""
1. 접근방법


"""

# n = int(input())
# cranes = list(map(int, input().split()))

# cranes.sort(reverse=True)

# m = int(input())
# boxs = list(map(int, input().split()))

# boxs.sort(reverse=True)

# if boxs[0] > cranes[0]:
#     print(-1)
#     exit()

# time = 0
# while len(boxs) != 0:
#     time += 1

#     check_cnt = 0
#     if len(boxs) >= len(cranes):
#         check_cnt = len(cranes)
#     else:
#         check_cnt = len(boxs)

#     moved_box = 0
#     for i in range(check_cnt):
#         if cranes[i] < boxs[i]:
#             break
        
#         moved_box += 1

#     boxs = boxs[moved_box:]

# print(time)



n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

# ⚡ 내림차순 정렬
crane.sort(reverse = True)
box.sort(reverse = True)

time = 0 # 시간
box_idx = 0

"""
9 8 6

7 5 4 2 2

"""

if max(box) > max(crane):
    print(-1)
else:
    while True:
        if box_idx == m-1:
            print(time)
            break

        for i in range(n):
            if crane[i] >= box[box_idx]:
                if box_idx == m-1:
                    break
                box_idx += 1

        time += 1



        
            