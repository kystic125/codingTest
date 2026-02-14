from collections import deque

def bfs(s):
    visited = [False] * (n+1)
    dst = [0] * (n+1)
    dq = deque([s])
    visited[s] = True

    while dq:
        v = dq.popleft()

        for next in lst[v]:
            if not visited[next]:
                visited[next] = True
                dst[next] = dst[v] + 1
                dq.append(next)

    return sum(dst[1:])

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

minValue = float('inf')
result = 0

for i in range(1, n+1):
    value = bfs(i)
    if value < minValue:
        minValue = value
        result = i

print(result)