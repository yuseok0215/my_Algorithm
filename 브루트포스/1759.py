vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
words = input().split()

words.sort() 

def check(arr):
    v_count, c_count = 0, 0 # 모음 개수, 자음 개수

    for i in arr:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

def backtracking(arr):

    if len(arr) == L:
        if check(arr):
            print("".join(arr))
            return

    for i in range(len(arr), C):
        if arr[-1] < words[i]:
            arr.append(words[i])
            backtracking(arr)
            arr.pop()

for i in range(C - L + 1): # 암호문 첫번째 문자로 사용할 수 있는 범위
    a = [words[i]]
    backtracking(a)





import sys


def back_tracking(cnt, idx):

    # 암호를 만들었을 때
    if cnt == l:
        # 모음, 자음 체크
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in consonant:
                vo += 1
            else:
                co += 1

        # 모음 1개 이상, 자음 2개 이상
        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    # 반복문을 통해 암호를 만든다.
    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(cnt + 1, i + 1) # 백트래킹
        answer.pop()


l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
consonant = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0, 0)