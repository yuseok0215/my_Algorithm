N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice)-max(dice))
else:
    sumList = [min(dice[0], dice[5]), # 마주보는 면
               min(dice[1], dice[4]),
               min(dice[2], dice[3])]
    sumList.sort()

    n1 = (N-2)*(N-2) + (N-1)*(N-2)*4 # 위쪽, 옆 4면
    n2 = (N-2)*4 + (N-1)*4 # 두면만 보이는 주사위
    n3 = 4

    ans = n1 * sumList[0] + n2 * sum(sumList[:2]) + n3 * sum(sumList)
    print(ans)

    """
    1. 접근방법
    일단 마주보는 면중에 작은 값을 선택..!
    그리고 면이 어떻게 보이는지 확인해보자(식 구하기)
    
    """