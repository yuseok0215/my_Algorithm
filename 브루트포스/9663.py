n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x): 
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): 
            # 세로 대각선
            return False
     
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.(0,0) (0,1) (0,2)  
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)