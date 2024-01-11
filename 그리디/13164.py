import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

arr = []
for i in range(1, n):
    arr.append(kids[i] - kids[i-1])

arr.sort(reverse=True)
print(sum(arr[k-1:]))


"""
1. 접근방법

두 수의 차이를 arr에 담고 그것들을 내림차순 한뒤에
제일 큰 차이들을 끊어주면 묶음이 생긴다.

1 3 5 6 10
 2 4 5   1 
   2 1

"""