n = int(input())
m = int(input())
s = list(input())

result = 0
check = list("IOI")
cnt = 0
i = 0

while i < m-2:
    if s[i:i+3] == check:
        cnt += 1
        i += 2
        
        if cnt >= n:
            result += 1

    else:
        cnt = 0
        i += 1
        
print(result)