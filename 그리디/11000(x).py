"""
s->t n개의 수업, 최소의 강의실에서 수업 가능하게.. 

1. 접근방법
순차적으로 돌면서 강의 끝나는 시간을 업데이트하고 다음 시작할 강의를 찾으면
다시 강의 끝나는 시간을 업데이트하자 
for문 한번 돌면 분명 남아있는 강의가 있을 것이다
이건 while문으로 리스트내에 남아있는 강의가 없을 경우 빠져나오도록 하자.
"""

n = int(input())

lec = []
for i in range(n):
    a,b = map(int, input().split())
    lec.append((a,b))


room = 1

end_time = []
end_time.append(lec[0][1])
for i in range(1,n):

    pass_idx = 0
    for j in range(len(end_time)):
        if lec[i][0] >= end_time[j]:
            pass_idx = j

    for j in range(pass_idx):
        end_time.pop(j)

    if len(end_time) == 0:
        room += 1
        end_time.append(lec[i][1])

    if end_time[0] <= lec[i][0]: #시작 시간이 더 뒤일때
        continue

    room += 1
    end_time.append(lec[i][1])
print(room)