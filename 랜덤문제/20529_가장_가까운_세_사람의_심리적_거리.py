t = int(input())

for _ in range(t):
    n = int(input())
    mbti = list(input().split())

    _min = 1e9

    flag = False
    for m in mbti: # mbti가 3개 이상일 때
        cnt = mbti.count(m)
        if cnt >= 3:
            print(0)
            flag = True
            break
    
    if flag:
        continue

    ans = 100000
    p = []

    def dfs(start):
        global ans
        if len(p)==3:
            temp = 0
            for i in range(4):
                if(p[0][i]!=p[1][i]):
                    temp +=1
                if(p[1][i]!=p[2][i]):
                    temp +=1
                if(p[2][i]!=p[0][i]):
                    temp +=1
            ans = min(ans,temp)
            return
        for i in range(start,n):
            p.append(mbti[i])
            dfs(i+1)
            p.pop()
    dfs(0)
    print(ans)
    