"""
1. 접근방법

"""
n,l = map(int, input().split())
fix_location = list(map(int, input().split()))

fix_range = l-1

start_location = 0
tape_count = 1
for i in range(1,n):
    if fix_location[i] - fix_location[start_location] <= fix_range: 
        # 현재 테이프로 막을 수 있는 범위일 때
        continue
    else:
        start_location = i
        tape_count += 1

if l == 1:
    tape_count = n

print(tape_count)