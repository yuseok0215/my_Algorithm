n,m = map(int, input().split())
trees = list(map(int, input().split()))

hei = max(trees) - min(trees)

while True:
    
    length = 0

    for tree in trees:
        if tree > hei:
            length += tree - hei

    if length == m:
        print(hei)
        break

    elif length < m:
        hei -= 1
    
    elif length > m:
        hei += 1