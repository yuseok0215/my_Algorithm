from itertools import combinations

while True:
    k = list(map(int, input().split()))
    if k[0] == 0:
        break
    arr = k[1:]

    combi_arr = list(combinations(arr, 6))
    
    for i in range(len(combi_arr)):
        for i in combi_arr[i]:
            print(i, end=' ')
        print()
    print()


