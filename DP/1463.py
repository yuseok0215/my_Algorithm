n = int(input())
d = [0] * (n + 1)	 

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1 # 1을 빼는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)	
        # 3으로 나눌 수 있으면 3을 나눈 수의 가중값을 가져와서 업데이트 한다. 
        # 1을 빼는 경우와 비교했을 때 어떤 것이 더 최솟값인가!
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n]) # 최종적으로 구하고자 하는 n까지의 값에 도달하게 된다.

