"""
정수 A -> B로 바꾸려고 한다.

2를 곱한다. 1을 수의 가장 오른쪽에 추가한다.
*10 + 1

뭔가 A->B 어렵다.. 그렇다면 B->A 해볼까..?
1. 끝자리가 1이면 1을 빼자.
2. 2로 나눌 수 있으면 나누자

"""

a,b = map(int, input().split())

oper_count = 1

while True:
    if b%10 != 1 and b%2 != 0 or a>b:
        print(-1)
        break

    if b%10 == 1:
        b -= 1
        b = b//10
        oper_count += 1

    if a == b: 
        print(oper_count)
        break
    
    if b%2 == 0:
        b = b//2
        oper_count += 1

    if a == b: 
        print(oper_count)
        break

    