from itertools import permutations

n, m = map(int, input().split())
lst = sorted(map(int, input().split()))

for i in permutations(lst, m):
    print(*i)
