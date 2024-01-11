N, K = map(int, input().split())

purchased_water_bottle_cnt = 0

while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    purchased_water_bottle_cnt += 2**idx
    N += 2**idx

print(purchased_water_bottle_cnt)

"""
1. 접근방법
작은 것 두개를 계속 합친다..! 
"""