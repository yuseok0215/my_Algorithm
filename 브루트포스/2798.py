"""
카드 합이 21이하, 합을 최대로 만든다.


"""

n, m = map(int, input().split())
num = list(map(int, input().split()))

num_res = []
for x in range(n):
    for y in range(n):
        for z in range(n):
            tmp = num[x] + num[y] + num[z]

            if tmp <= m and x != y and y != z and z != x:
                num_res.append(tmp)

num_res.sort(reverse=True)

print(num_res[0])



