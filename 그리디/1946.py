"""
서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
선발할 수 있는 최대 인원 수 구하기..

A, B 분류의 성적이 주어진다.
1 4 p
2 3 p
3 2 p
4 1 p
5 5 np

1 4 p
2 5 np
3 6 np
4 2 p
5 7 np
6 1 p
7 3 np


"""

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    grade = []

    for j in range(n):
        a,b = map(int, input().split())
        grade.append((a,b))

    sorted_grade = sorted(grade, key=lambda x: x[0])
    pass_people = 1

    max_grade = sorted_grade[0][1]
    for idx in range(1,n):
        if sorted_grade[idx][1] < max_grade:
            max_grade = sorted_grade[idx][1]
            pass_people += 1
            
    print(pass_people)