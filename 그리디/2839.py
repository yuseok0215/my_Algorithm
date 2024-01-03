n = int(input())

five_kg = n//5 
rest_kg = n%5 # 5킬로 묶음을 제외한 나머지 수량

answer = 0

while True:
    if five_kg == -1:
        answer = -1
        break

    three_kg = rest_kg//3

    if rest_kg%3 == 0:
        answer = three_kg + five_kg
        break

    five_kg -= 1
    rest_kg += 5

print(answer)


"""
 봉지는 3, 5 배달할 양은 N
 최대한 적은 봉지
 1. 접근 방법
 일단 5킬로로 최대 수량을 만들고 나머지 수량을 3킬로로 채워보자
 만약 나머지 수량이 3킬로로 채워지지 않는다면 5킬로 하나씩 빼면서 채워보자

 3. 시간복잡도 
 O(n)
"""
