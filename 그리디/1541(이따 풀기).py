n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

minus = []
plus = []
result = 0
zero_cnt = 0
for num in nums:
    if num < 0:
        minus.append(num)
    elif num > 1:
        plus.append(num)
    elif num == 1:
        result += 1
    elif num == 0:
        zero_cnt += 1

minus.sort()
plus.sort(reverse=True)

for i in range(0,len(minus),2):
    if i == len(minus)-1:
        if zero_cnt > 0:
            continue
        result += minus[i]
        continue

    result += minus[i] * minus[i+1]
    i += 1 

for i in range(0,len(plus),2):
    if i == len(plus)-1:
        result += plus[i]
        continue

    result += plus[i] * plus[i+1]
    i += 1 

print(result)