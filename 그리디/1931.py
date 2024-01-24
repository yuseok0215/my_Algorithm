"""
1. 접근방법
일단 현재 가장 빨리 시작할 수 있는 회의를 선택하고 두개 이상이라면 
가장 빨리 끝나는 회의를 선택해보자.

"""

n = int(input())
meeting = []
meeting_count = 0
for i in range(n):
    a,b = list(map(int, input().split()))
    meeting.append((a,b))

sorted_meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

current_start = 0
current_end = 0
for start, end in sorted_meeting:
    if current_end <= start:
        current_start = start
        current_end = end
        meeting_count += 1

print(meeting_count)
