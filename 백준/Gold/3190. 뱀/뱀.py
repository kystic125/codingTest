n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
commands = []
for _ in range(l):
    t, command = input().split()
    commands.append((int(t), command))

snake = [[0, 0]]
cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

while True:
    cnt += 1
    x, y = snake[0]
    nx, ny = x + dx[d], y + dy[d]

    if [nx, ny] in snake or nx < 0 or ny < 0 or nx >= n or ny >= n:
        break
    else:
        if board[nx][ny] == 1:
            snake.insert(0, [nx, ny])
            board[nx][ny] = 0
        else:
            snake.insert(0, [nx, ny])
            snake.pop()

    if commands and cnt == commands[0][0]:
        t, c = commands.pop(0)
        if c == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

print(cnt)
