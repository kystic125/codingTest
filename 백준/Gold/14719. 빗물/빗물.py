h, w = map(int, input().split())

lst = list(map(int, input().split()))
result = 0

for i in range(1, len(lst)-1):
    lmax, rmax = 0, 0
    for j in range(0, i):
        if lst[j] > lmax:
            lmax = lst[j]
    for k in range(i+1, len(lst)):
        if lst[k] > rmax:
            rmax = lst[k]
    
    mValue = min(lmax, rmax)

    value = mValue - lst[i]

    if value > 0:
        result += value

print(result)