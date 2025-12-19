n = int(input())
result = []
for _ in range(n):
    stack = []
    parentheses = input()
    for i in parentheses:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break

    if stack:
        result.append("NO")
    else:
        result.append("YES")
        
for i in result:
    print(i)