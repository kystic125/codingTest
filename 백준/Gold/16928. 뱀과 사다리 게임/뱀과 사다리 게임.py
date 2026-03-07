from collections import deque

def bfs():
    visited = [False] * 101
    dq = deque([(1, 0)])
    visited[1] = True

    while dq:
        s, count = dq.popleft()
        
        for i in range(1, 7):
            ns = s + i

            if ns in move:
                ns = move[ns]

            if ns == 100:
                return count + 1

            if not visited[ns]:
                visited[ns] = True
                dq.append((ns, count + 1))

n, m = map(int, input().split())

move = {}

for _ in range(n):
    x, y = map(int, input().split())
    move[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    move[x] = y

print(bfs())