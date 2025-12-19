def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        size = 1
        size += dfs(x-1, y)
        size += dfs(x+1, y)
        size += dfs(x, y-1)
        size += dfs(x, y+1)
        return size
    return 0
        


n = int(input())
count = 0
graph = []
sizes = []

for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        size = dfs(i, j)
        if size > 0:
            count += 1
            sizes.append(size)
sizes.sort()
print(count)
for i in sizes:
    print(i)