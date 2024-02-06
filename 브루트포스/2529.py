k = int(input())
arr = list(input().split())


def check(i,j,k):
    if k == '<':
        return i < j
    else:
        return i > j

def dfs(depth, s):
    global _max, _min

    if depth == k+1:
        if len(_min) == 0:
            _min = s
        else:
            _max = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), arr[depth-1]):
                visited[i] = True
                dfs(depth+1, s+str(i))
                visited[i] = False  

_max = ''
_min = ''

visited = [False] * 10
result = ''

print(_max)
print(_min)