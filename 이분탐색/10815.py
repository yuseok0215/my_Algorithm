n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check_nums = list(map(int, input().split()))

cards.sort()

for num in check_nums:
    low, high = 0, n-1
    exist = False

    while low <= high:
        mid = (low+high) // 2
        if cards[mid] > num:
            high = mid - 1
        elif cards[mid] < num:
            low = mid + 1
        else:
            exist = True
            break
    
    if exist:
        print(1, end=' ')
    else:
        print(0, end=' ')


## 딕셔너리 풀이법
# import sys

# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# checks = list(map(int, sys.stdin.readline().split()))

# _dict = {}  # 속도는 dictionary!
# for i in range(len(cards)):
#     _dict[cards[i]] = 0  # 아무 숫자로 mapping

# for j in range(M):
#     if checks[j] not in _dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')