"""
k개 숫자를 앞에서부터 뺐을 때 일단 가능한 높은 숫자까지 숫자를 제거하자.



작은 숫자를 먼저 빼고
작은 숫자끼리중에는 뒤에 있는 숫자부터 뺀다.

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()
stack = []
for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))




# max_num = 0
# max_idx = 0
# for i in range(k):
#     if max_num < num_arr[i]:
#         max_num = num_arr[i]
#         max_idx = i

# num_arr = num_arr[i-1:]
# k -= max_idx

# # 77252841
# idx = 0
# for idx in range(len(num_arr)-1):
#     if k == 0:
#         break

#     if num_arr[idx] < num_arr[idx+1]:
#         num_arr.pop(idx)
#         k -= 1
#         continue

#     idx += 1
    
# if k != 0:
#     for _ in range(k):
#         num_arr.pop()
    
# answer = ''
# for elem in num_arr:
#     answer += str(elem)

# print(answer)






