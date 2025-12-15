n = int(input())
stack = []
result = []

for _ in range(n):
    command = input().split()
    
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif command[0] == 'size':
        result.append(len(stack))
    elif command[0] == 'empty':
        if stack:
            result.append(0)
        else:
            result.append(1)
    else:
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

for i in result:
    print(i)