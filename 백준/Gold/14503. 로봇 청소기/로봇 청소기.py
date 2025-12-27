n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]

while True:
    if graph[x][y] == 0:
        graph[x][y] = -1
    neighbor = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny] == 0:
            neighbor = True
    if not neighbor:
        back = (d+2) % 4
        nx, ny = x+dx[back], y+dy[back]
        if graph[nx][ny] == 1:
            break
        x, y = nx, ny
    else:
        d = (d+3) % 4
        nx, ny = x+dx[d], y+dy[d]
        if graph[nx][ny] == 0:
            x, y = nx, ny

count = sum(row.count(-1) for row in graph)
print(count)