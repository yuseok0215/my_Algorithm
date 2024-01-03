N = int(input())

deque = []
command = []

for i in range(N):
    command.append(input())

for op in command:
    # operation = input().split("")

    operation = op.split()

    if(operation[0] == 'push_front'):
        deque.insert(0,operation[1])
    
    elif(operation[0] == 'push_back'):
        deque.append(operation[1])

    elif(operation[0] == 'pop_front'):
        if(len(deque) == 0):
            print(-1)
        elif(len(deque) != 0):
            print(deque[0])
            deque.pop(0)
    
    elif(operation[0] == 'pop_back'):
        if(len(deque) == 0):
            print(-1)
        elif(len(deque) != 0):
            print(deque[-1])
            deque.pop()
    
    elif(operation[0] == 'size'):
        print(len(deque))

    elif(operation[0] == 'empty'):
        if(len(deque) == 0):
            print(1)
        elif(len(deque) != 0):
            print(0)

    elif(operation[0] == 'front'):
        if(len(deque) == 0):
            print(-1)
        elif(len(deque) != 0):
            print(deque[0])
            
    elif(operation[0] == 'back'):
        if(len(deque) == 0):
            print(-1)
        elif(len(deque) != 0):
            print(deque[-1])        
    