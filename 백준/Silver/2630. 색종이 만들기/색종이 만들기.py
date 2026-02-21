def func(x, y, size):
    value = graph[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if value != graph[i][j]:
            
                newSize = size // 2

                func(x, y, newSize)
                func(x, y+newSize, newSize)
                func(x+newSize, y, newSize)
                func(x+newSize, y+newSize, newSize)
                return
            
    if value == 0:
        count[0] += 1
    else:
        count[1] += 1

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0]

func(0, 0, n)

print(count[0])
print(count[1])
