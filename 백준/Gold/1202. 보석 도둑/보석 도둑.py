import heapq
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

jewel = []
bag = []

jewel = [tuple(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

jewel.sort()
bag.sort()

lst = []
result = 0
idx = 0

for size in bag:
    while idx < n and jewel[idx][0] <= size:
        heapq.heappush(lst, -jewel[idx][1])
        idx += 1

    if lst:
        result += -heapq.heappop(lst)

print(result)