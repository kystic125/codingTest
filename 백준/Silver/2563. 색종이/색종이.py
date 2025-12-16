n = int(input())
lst = [[0] * 100 for _ in range(100)]


for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            lst[x+i][y+j] = 1


result = 0

for i in lst:
    result += sum(i)

print(result)