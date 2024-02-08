t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0:
        print(1, 0)
        continue
    elif n == 1:
        print(0, 1)
        continue

    one_cnt = 0
    zero_cnt = 0

    dp_zero = [0] * (n+1)
    dp_one = [0] * (n+1)
    
    dp_one[0] = 0
    dp_one[1] = 1
    
    dp_zero[0] = 1
    dp_zero[1] = 0

    for i in range(2, n+1):
        dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
        dp_one[i] = dp_one[i-1] + dp_one[i-2]

    print(dp_zero[n], dp_one[n])