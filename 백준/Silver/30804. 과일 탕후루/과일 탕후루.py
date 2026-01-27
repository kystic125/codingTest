n = int(input())
s = list(map(int, input().split()))
dct = {}
l, r = 0, 0
m = 0

while r < n:
    dct[s[r]] = dct.get(s[r], 0) + 1

    while len(dct) > 2:
        dct[s[l]] -= 1

        if dct[s[l]] == 0:
            del dct[s[l]]
        l += 1

    m = max(m, r - l + 1)
    r += 1

print(m)