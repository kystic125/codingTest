import heapq
from sys import stdin
input = stdin.readline

lst = []
result = []
N = int(input())

for _ in range(N):
    n = int(input())

    if n > 0:
        heapq.heappush(lst, -n)
    else:
        if lst:
            print(-heapq.heappop(lst))
        else:
            print(0)
