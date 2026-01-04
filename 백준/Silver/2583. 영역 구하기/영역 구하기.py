from collections import deque

def bfs(graph, visited, x, y, count):
    dq = deque([(x, y)])
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                count += 1
                dq.append((nx, ny))
    
    return count


m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[m-1-y][x] = 1
            
area = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            count = 1
            area.append(bfs(graph, visited, i, j, count))

area.sort()

print(len(area))
for i in area:
    print(i, end=' ')