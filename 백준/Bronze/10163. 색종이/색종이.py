n = int(input())
graph = [[0] * 1010 for _ in range(1010)]
result = [0] * (n+1)

for k in range(1, n+1):
    a, b, c, d = map(int, input().split())

    for i in range(a, a+c):
        graph[i][b:b+d] = [k] * d


for i in range(1010):
    for j in range(1010):
        if graph[i][j] != 0:
            result[graph[i][j]] += 1

for i in range(1, n + 1):
    print(result[i])