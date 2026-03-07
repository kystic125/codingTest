tc = int(input())

lst = []
for _ in range(tc):
    lst.append(int(input()))

n = max(lst)
dp = [0] * (n + 1)

if n >= 1: dp[1] = 1
if n >= 2: dp[2] = 1
if n >= 3: dp[3] = 1

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-3]

for i in lst:
    print(dp[i])