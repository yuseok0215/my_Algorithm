n, m = map(int, input().split())

book = list(map(int, input().split()))

plus = []
minus = []
max_loc = 0
for elem in book:
    if max_loc < abs(elem):
        max_loc = abs(elem)

    if elem > 0:
        plus.append(elem)
    elif elem < 0:
        minus.append(elem)

plus.sort(reverse=True) # 50 45 10
minus.sort() # -50 -30 -20

idx = 0
result = 0
while len(plus) > 0:
    if idx > len(plus)-(m+1):
        result += plus[idx] * 2
        break

    result += plus[idx] * 2
    idx += m

idx = 0
while len(minus) > 0:
    if idx > len(minus)-(m+1):
        result += abs(minus[idx]) * 2
        break

    result += abs(minus[idx]) * 2
    idx += m 


print(result - max_loc)
    

# -5 -2 1 5 10 12