from collections import deque

def bfs(graph, dq):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))

    return graph


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dq = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dq.append((i, j))
        

result = bfs(graph, dq)

if any(0 in row for row in result):
    print(-1)
else:
    print(max(max(row) for row in result) -1)