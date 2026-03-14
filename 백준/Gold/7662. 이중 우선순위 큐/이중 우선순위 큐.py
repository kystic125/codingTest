import heapq
from sys import stdin
input = stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    minHeap = []
    maxHeap = []
    visited = [False] * n

    for i in range(n):
        command, num = input().split()
        num = int(num)
        if command == 'I':    
            heapq.heappush(minHeap, (num, i))
            heapq.heappush(maxHeap, (-num, i))
            visited[i] = True
        elif command == 'D':
            if num == 1:
                while maxHeap and not visited[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
            else:
                while minHeap and not visited[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)

    while maxHeap and not visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)

    if minHeap and maxHeap:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")