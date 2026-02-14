def func(x, y, size):
    lst = []
    value = graph[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if value != graph[i][j]:
            
                newSize = size // 2

                print("(", end="")
                func(x, y, newSize)
                func(x, y+newSize, newSize)
                func(x+newSize, y, newSize)
                func(x+newSize, y+newSize, newSize)
                print(")", end="")
                return
            
    print(value, end="")

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

func(0, 0, n)