from collections import deque

dq = deque()
num = int(input())
result = []

for i in range(num):
    cmd = input().split()

    if cmd[0] == 'push':
        dq.append(cmd[1])
    elif cmd[0] == 'pop':
        if dq:
            result.append(dq.popleft())
        else:
            result.append(-1)
    elif cmd[0] == 'size':
        result.append(len(dq))
    elif cmd[0] == 'empty':
        if len(dq) == 0:
            result.append(1)
        else:
            result.append(0)
    elif cmd[0] == 'front':
        if len(dq) == 0:
            result.append(-1)
        else:
            result.append(dq[0])
    elif cmd[0] == 'back':
        if dq:
            result.append(dq[-1])
        else:
            result.append(-1)
            
for i in result:
    print(i)