# n,k = map(int, input().split())

# numbers = []
# answer_numbers = []
# delete_index = 0
# move_amount = k-1

# for i in range(1,n+1):
#     numbers.append(i)

# while(len(numbers) != 0):
#     if(delete_index + move_amount < len(numbers)):
#         delete_index += move_amount

#     elif(k >= len(numbers)):
#         check_number = move_amount
#         while True:
#             move_amount -= len(numbers)

#             if(move_amount < len(numbers)):
#                 if(delete_index + move_amount < len(numbers)):
#                     delete_index += move_amount
#                 elif(delete_index + move_amount >= len(numbers)):
#                     rest_amount = move_amount - (len(numbers)-1-delete_index)
#                     delete_index = rest_amount - 1
#                 break    


#     elif(delete_index + move_amount >= len(numbers)):
#         rest_amount = move_amount - (len(numbers)-1-delete_index)
#         delete_index = rest_amount - 1
    
    
    
#     answer_numbers.append(numbers[delete_index])
#     numbers.pop(delete_index)


# print("<", end = '')
# for elem in answer_numbers:
#     print(str(elem), end = ', ')
# print(">")


n,k = map(int, input().split())

numbers = []
answer = []

for i in range(1,n+1):
    numbers.append(i)

delete_index = 0
move_idx = k-1

while len(numbers) != 0:
    delete_index += move_idx
    if delete_index >= len(numbers):
        delete_index = delete_index % len(numbers)

    answer.append(str(numbers.pop(delete_index)))

print("<" + ", ".join(map(str, answer)) + ">")


    


"""
1. 접근 방법
[1,2,3,4,5,6,7]  3
-> [1,2,4,5,6,7]  6
-> [1,2,4,5,7]  2

인덱스 + 2 로 해결해야할 것 같다?

2. 핵심 알고리즘
%의 쓰임을 이해하고 있기

3. 시간 복잡도
O(n)

4. 다른 방법

from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
answer = []
 
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
 
print(str(answer).replace('[', '<').replace(']', '>'))
"""

