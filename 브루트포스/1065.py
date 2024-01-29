n = int(input())

cnt = 0
for i in range(1,n+1):
    if i // 100 < 1:
        cnt += 1
        continue

    str_ = str(i)
    tmp = int(str_[1]) - int(str_[0])
    for i in range(1, len(str_)-1):
        if tmp != int(str_[i+1]) - int(str_[i]):
            break

        cnt += 1

print(cnt)

