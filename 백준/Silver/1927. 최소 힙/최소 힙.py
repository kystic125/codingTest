from sys import stdin
import heapq
input = stdin.readline

num = int(input())

heap = []
result = []

for i in range(num):
    n = int(input())

    if n > 0:
        heapq.heappush(heap, n)
    elif n == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)

for i in result:
    print(i)
