numbers = []

for i in range(1,10000):
    number = str(i)
    all_sum = 0
    for elem in number:
        all_sum += int(elem)
    numbers.append(all_sum + i)

unique_numbers = list(set(numbers))

for i in range(1,10000):
    if i not in unique_numbers:
        print(i)

"""
1. 접근 방법
각자리 수를 어떻게 추출할 것인가? 
-> 수작업으로 1, 10, 100, 1000의 각 자리를 구하여 더해주자.
-> 너무 비효율적이고 만약 원하는 범위가 달라졌을 때 재사용이 불가능하다.
형변환을 이용한다면?
-> 문자열로 변환한 뒤에 각 자리를 순회하면서 다시 int타입으로 형변환하여 합을 구해보자

2. 문제의 핵심 알고리즘
형변환을 이용하는 것

3. 시간복잡도
O(n)

"""       