n = int(input())
arr = list(map(int, input().split()))

arr.sort()
group = 0

for i in range(n):
    if i+arr[i] > n-1:
        break
    
    group += 1
    i += arr[i]

print(group)


