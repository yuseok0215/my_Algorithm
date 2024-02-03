k = int(input())
arr = list(input().split())


def dfs(idx, left_num, flag):
    global _max
    global _min

    if len(result) == k+1:
        combined_number = int(''.join(map(str, result)))
        _max = max(_max, combined_number)
        _min = min(_min, combined_number)
        return

    flag = False
    
    if arr[idx] == '<':
        for i in range(10):
            if i not in result and left_num < i:
                result.append(i)
                flag = True
                dfs(idx+1,i,flag)
                
                
    elif arr[idx] == '>':
        for i in range(10):
            if i not in result and left_num > i:
                result.append(i)
                flag = True
                dfs(idx+1,i,flag)

               
            
                    
_max = -1e9
_min = 1e9

for i in range(10):
    visited = [False] * 9
    result = [i]
    dfs(0,i,False)

print(_max)
print(_min)