def dfs(s, lst, visited):
    visited[s] = True
    cnt = 1
    for i in lst[s]:
        if not visited[i]:
            cnt += dfs(i, lst, visited)
    
    return cnt

m = int(input())
n = int(input())

lst = [[]for _ in range(m+1)]

for _ in range(n):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [False] * (m+1)

print(dfs(1, lst, visited) - 1)