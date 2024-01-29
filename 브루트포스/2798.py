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

# 더 빠른 풀이

N, M = map(int, input().split())
card_num = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j + 1, N):
            card_combi_sum = card_num[i] + card_num[j] + card_num[z]
            if card_combi_sum <= M:
                result = max(result, card_combi_sum)
                
print(result)

