from collections import deque

def bfs(graph, visited, n, m):
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))
                visited[nx][ny] = True
                
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [[False] * m for _ in range(n)]

print(bfs(graph, visited, n, m))
