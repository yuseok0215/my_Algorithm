import sys

input = sys.stdin.readline

n = int(input())

numbers = []

count = dict()
for i in range(n):
    number = int(input())
    numbers.append(number)

    if number in numbers:
        count[number] = 1
    else:
        count[number] += 1

a = int(sum(numbers))

if a >= 0:
    print(int(sum(numbers) / n + 0.5))
elif a < 0:
    print(int(sum(numbers) / n - 0.5))

numbers.sort()
print(numbers[n//2])

freq = max(count.values())

freq_numbers = []
for key, value in count.items():
    if value == freq:
        freq_numbers.append(key)

if len(freq_numbers == 1):
    print(freq_numbers[0])
else:
    print(sorted(freq_numbers)[1])

print(numbers[-1] - numbers[0])



