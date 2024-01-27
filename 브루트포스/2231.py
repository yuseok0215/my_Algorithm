n = int(input())

for i in range(1,n+1):
    str_num = str(i)
    
    result = i
    for num in str_num:
        result += int(num)

    if result == n:
        print(i)
        break