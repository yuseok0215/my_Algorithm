"""
음수를 극대화해야 한다.
- 뒤에서부터 괄호로 묶고 다시 +가 나오면 +앞에서 괄호를 닫아주자.

"""
import sys
input = sys.stdin.readline

#str_list = input().split('-') # '-'를 기준으로 나눈다.
str_list = list(map(str, sys.stdin.readline().strip().split('-')))

answer = 0

for i in str_list[0].split('+'):
    answer += int(i)

for i in str_list[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)