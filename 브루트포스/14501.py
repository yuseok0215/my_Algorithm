n = int(input())

sche = []
for _ in range(n):
    t,p = map(int, input().split())
    sche.append((t,p))

day = n
end = n+1
result = 0
while True:
    d, p = sche[day-1]
    if day + d <= end:
        day = d
        end -= d

        if day < 1:
            break

        result += p
    
    day -= 1

print(result)  