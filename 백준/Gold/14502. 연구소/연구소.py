from itertools import combinations
from collections import deque
import copy

def bfs(graph):
    dq = deque(virus)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dq.append((nx, ny))
    
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    return count

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

maxSafe = 0

for i in combinations(empty, 3):
    newGraph = copy.deepcopy(graph)
    for x, y in i:
        newGraph[x][y] = 1
    
    safe = bfs(newGraph)
    maxSafe = max(maxSafe, safe)

print(maxSafe)
