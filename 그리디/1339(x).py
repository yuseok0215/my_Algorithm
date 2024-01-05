"""
1. 접근방법

알파벳을 많이 가지고 있는 순으로 정렬한다.
ACDEB / GCF / BD
혹시 dictionary..?
"""

n = int(input())
arr = []

for _ in range(n):
    word = input()
    word_length = len(word)
    for i in range(word_length):
        arr[word_length-i].append(word[i])

print(arr)

        


    


