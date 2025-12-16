from collections import deque

def bfs(dq, graph, visited, n, m):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]        

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))
    
    return graph

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dq = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dq.append((i, j))

result = bfs(dq, graph, visited, n, m)

result = [x for row in result for x in row]

if 0 in result:
    print(-1)
else:
    print(max(result) - 1)