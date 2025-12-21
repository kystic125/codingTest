import sys
from collections import deque
input = sys.stdin.readline

def bfs(s, graph, visited):
    dq = deque([s])
    visited[s] = True
    
    while dq:
        s = dq.popleft()

        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i, graph, visited)
        cnt += 1

print(cnt)