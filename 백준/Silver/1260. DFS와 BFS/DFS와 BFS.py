from collections import deque

def dfs(lst, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in lst[v]:
        if not visited[i]:
            dfs(lst, i, visited) 

def bfs(lst, start, visited):
    dq = deque([start])
    visited[start] = True
    
    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for i in lst[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True
    
    
n, m, v = map(int, input().split())
lst = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in range(1, n + 1):
    lst[i].sort()
    
dfsvisited = [False] * (n + 1)
bfsvisited = [False] * (n + 1)

dfs(lst, v, dfsvisited)
print()
bfs(lst, v, bfsvisited)