import heapq
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

jewel = []
bag = []

for i in range(n):
    jewel.append(list(map(int, input().split())))

for i in range(k):
    bag.append(int(input()))

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