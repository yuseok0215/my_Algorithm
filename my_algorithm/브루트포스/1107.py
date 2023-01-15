import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
broken_num = list(map(int, input().split()))

min_cnt = abs(100-target)

for nums in range(1000001):
    nums = str(nums)

    for i in range(len(nums)):
        # 해당 nums에 고장난 숫자버튼이 들어있으면 패스
        if int(nums[i]) in broken_num:
            break
        # 고장난 숫자 없이 끝까지 도착했다면 해당 숫자 누른 버튼 수 + 그 숫자에서 타겟까지 +,- 누를 횟수
        elif i == len(nums) - 1:
            min_cnt = min(min_cnt, len(str(nums)) + abs(int(nums) - target))

print(min_cnt)


