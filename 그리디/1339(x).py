n = int(input())
alp = []
alp_dict = {}
num_list = []

for _ in range(n):
    alp.append(input())

for elem in alp:
    for j in range(len(elem)):
        if elem[j] in alp_dict:
            alp_dict[elem[j]] += 10 ** (len(elem)-j-1)
        else:
            alp_dict[elem[j]] = 10 ** (len(elem)-j-1)

for value in alp_dict.values():
    num_list.append(value)

num_list.sort(reverse=True)

sum = 0
w = 9
for i in num_list:
    sum += i*w
    w-=1

print(sum)


"""
1. 접근방법

ABCD이면 A에 1000, B에 100, C에 10 D에 1을 곱해주면 그 자릿수 값으로 치환할 수 있다.
근데 만약에 ACB, ABFGF 이런식으로 있으면 첫번째 A는 100을 담아주면 뒤에 있는 A 10000을 어떻게 담지?(이게 고민이었다..)
정답은 중복해서 담을 수 있게 합하는 것이었다. 100 + 10000 = 10100 이런식으로 하면 A가 등장한 자릿수들을 다 캐치할 수 있다.(이런 아이디어가 실전에서 생기면 코테 합격일듯..)
그래서 각 알파벳마다 등장한 자릿수들을 다 담아주고 자릿수 자체로 가장 높은 숫자들부터 0~9에서 가장 높은 숫자들로 채워넣기 위해
내림차순 정렬하고 9,8,7,,,, 을 차례로 곱해주고 합하면 끝이다..!


"""

        


    


