n = int(input())
graph = [[0] * 1001 for _ in range(1001)]
result = []

for k in range(1, n+1):
    a, b, c, d = map(int, input().split())

    for i in range(a, a+c):
        for j in range(b, b+d):
            graph[i][j] = k


for i in range(1, n+1):
    cnt = 0
    for a in graph:
        for b in a:
            if b == i:
                cnt += 1

    result.append(cnt)

for r in result:
    print(r)