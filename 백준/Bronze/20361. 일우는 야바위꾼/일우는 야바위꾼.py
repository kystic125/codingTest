n, x, k = map(int, input().split())

lst = [0] * (n+1)
lst[x] = 1

for _ in range(k):
    a, b = map(int, input().split())

    lst[a], lst[b] = lst[b], lst[a]

print(lst.index(1))