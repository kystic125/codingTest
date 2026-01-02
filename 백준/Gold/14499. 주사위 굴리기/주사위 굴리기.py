n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
direction = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    d = direction[i]
    nx, ny = x + dx[d-1], y + dy[d-1]

    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny

        if d == 1:
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
        elif d == 2:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
        elif d == 3:
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
        elif d == 4:
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

        if graph[x][y] == 0:
            graph[x][y] = dice[1]
        else:
            dice[1] = graph[x][y]
            graph[x][y] = 0

        print(dice[0])