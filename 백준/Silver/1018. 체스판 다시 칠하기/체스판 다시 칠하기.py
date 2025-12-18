n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = []

for i in range(n-7):
    for j in range(m-7):
        cnt = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    color = "W"
                else:
                    color = "B"

                if board[x][y] != color:
                    cnt += 1
    
        result.append(min(cnt, 64-cnt))
        
print(min(result))