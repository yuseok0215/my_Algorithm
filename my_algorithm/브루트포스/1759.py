import sys
input = sys.stdin.readline

l, c = map(int, input().split())
alp = sorted(list(map(str, input().split())))

vowels = ['a', 'e', 'i', 'o', 'u']
answer = []

def back_tracking(cnt, idx):

    if cnt == l:
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in vowels:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(alp[i])
        back_tracking(cnt + 1, i + 1) # 백트래킹
        answer.pop()

back_tracking(0,0)
