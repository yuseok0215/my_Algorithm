k = int(input())

numbers = []

for i in range(k):
    number = int(input())

    if(number == 0):
        numbers.pop()

    elif(number != 0):
        numbers.append(number)

print(sum(numbers)) 
